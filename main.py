import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import MAX_ITERATIONS
from prompts import system_prompt
from functions.call_function import call_function
from functions.schemas import (
    schema_get_file_content,
    schema_get_files_info,
    schema_run_python_file,
    schema_write_file,
)


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="AI Agent poweredy by Gemini 2.0 Flash"
    )

    parser.add_argument("prompt", type=str, help="The prompt to send to the AI agent.")

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output."
    )

    args = parser.parse_args()
    user_prompt = args.prompt
    is_verbose = args.verbose

    if is_verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_file_content,
            schema_get_files_info,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    i = 0
    while i < MAX_ITERATIONS:
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_prompt
                ),
            )

            # Candidates provide reasoning and context for the model for the
            # whole conversation
            if response.candidates:
                for candidate in response.candidates:
                    if candidate.content:
                        messages.append(candidate.content)

            # Function calls are the concrete actions to be executed
            # from the reasoning provided in candidates
            if response.function_calls:
                for function_call_part in response.function_calls:
                    content = call_function(function_call_part, verbose=is_verbose)
                    messages.append(content)

            # If there's a text response, assume there's no more actions to
            # be taken, so we can print the final result
            elif response.text:
                print(f"Final response:\n{response.text}")
                break

            i += 1

        except Exception as e:
            print(f"An error occurred: {e}")
            break


if __name__ == "__main__":
    main()

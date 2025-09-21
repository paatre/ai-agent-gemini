import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import call_function
from functions.schemas import (
    schema_get_file_content,
    schema_get_files_info,
    schema_run_python_file,
    schema_write_file
)


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        sys.exit("No content was given for the Gemini client. Exiting.")

    is_verbose = False
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        is_verbose = True

    user_prompt = sys.argv[1]

    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=user_prompt )]
        )
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_file_content,
            schema_get_files_info,
            schema_run_python_file,
            schema_write_file
        ]
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt)
    )

    if response.function_calls:
        for function_call_part in response.function_calls:
            content = call_function(function_call_part, verbose=is_verbose)

            if (
                (parts := content.parts) and
                (function_response := parts[0].function_response) and
                (result := function_response.response)
            ):
                if not result:
                    raise Exception("Function call did not return any result.")

                if is_verbose:
                    print(f"-> {result["result"]}")
    else:
        print(response.text)

    if is_verbose:
        print(f"User prompt: {user_prompt}")
        if response.usage_metadata:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()

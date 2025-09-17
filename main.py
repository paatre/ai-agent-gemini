import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


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

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    print(response.text)

    if is_verbose:
        print(f"User prompt: {user_prompt}")
        if response.usage_metadata:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()

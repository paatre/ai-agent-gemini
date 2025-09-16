# AI Agent with Gemini (Boot.dev)

This is a simple AI Agent project that utilizes Google's Gemini model's
free tier to perform various tasks. This project follows the course on Boot.dev
platform: https://www.boot.dev/courses/build-ai-agent-python.

The project is built using Python and
[Google's Gen AI SDK](https://googleapis.github.io/python-genai/).

## Setup

First, clone the repository:

```bash
git clone https://github.com/paatre/ai-agent-gemini-bootdev.git
```

After that navigate to the project directory and install the dependencies:

```bash
cd ai-agent-gemini-bootdev
uv venv
source .venv/bin/activate # On Windows use `.\venv\Scripts\activate`
uv sync
```

To use the Gemini client, you need to set up a Google AI Studio account and
obtain an API key which the client will use for authentication. You can do that
from the Google AI Studio directly: https://aistudio.google.com/apikey. You
need to sign in with your Google account. Note that you need a project which
the API key will be associated with but the Google AI Studio will do that for
you automatically.

After you have your API key, set it to an `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

The `.env` file will be loaded automatically by the `python-dotenv` package.
The `.env` file is included in `.gitignore`.

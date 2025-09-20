from google.genai import types


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets text contents from a file, truncates after the first 10000 characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read content from, relative to the working directory. Returns an error if a regular file is not given.",
            ),
        },
    ),
)


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a given Python file and returns the output(s). Timeouts in 30 seconds. Captures stdout and stderr.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the executable Python file. The file needs to be located relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING
                ),
                description="Extra arguments for the executable Python file in a list format. Defaults to an empty list if no extra arguments are given.",
            ),
        },
    ),
)


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes given content to a file. Writing overwrites possible existing content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path where given content is written to. File path is relative to the working directory. Intermediate directories are created if they don't exist yet.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content in text format which is written to the file path.",
            ),
        },
    ),
)

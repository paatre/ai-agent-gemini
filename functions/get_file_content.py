import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        file_full_path = os.path.join(working_directory, file_path)
        abs_work_dir = os.path.abspath(working_directory)
        abs_file_full_path = os.path.abspath(file_full_path)

        if not abs_file_full_path.startswith(abs_work_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_full_path, "r") as f:
            content = f.read(MAX_CHARS)
            if len(content) > MAX_CHARS:
                content += f'[...File "{file_path}" truncated at 10000 characters]'
            return content

    except Exception as e:
        return f"Error: {e}"

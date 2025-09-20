import os


def write_file(working_directory, file_path, content):
    try:
        file_full_path = os.path.join(working_directory, file_path)
        abs_work_dir = os.path.abspath(working_directory)
        abs_file_full_path = os.path.abspath(file_full_path)

        if not abs_file_full_path.startswith(abs_work_dir):
            return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"

        if not os.path.exists(abs_file_full_path):
            os.makedirs(os.path.dirname(abs_file_full_path), exist_ok=True)

        with open(abs_file_full_path, "w") as f:
            chars_written = f.write(content)
            if chars_written > 0:
                return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"

    except Exception as e:
        return f"Error: {e}"


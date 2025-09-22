import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        file_full_path = os.path.join(working_directory, file_path)
        abs_work_dir = os.path.abspath(working_directory)
        abs_file_full_path = os.path.abspath(file_full_path)

        if not os.path.commonpath([abs_work_dir, abs_file_full_path]) == abs_work_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(abs_file_full_path):
            return f'Error: File "{file_path}" not found.'

        if not abs_file_full_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        completed_process = subprocess.run(
            ["python", abs_file_full_path, *args],
            timeout=30,
            capture_output=True,
            cwd=abs_work_dir,
            text=True,
        )

        stdout = completed_process.stdout.strip()
        stderr = completed_process.stderr.strip()
        return_code = completed_process.returncode

        output = []

        if stdout:
            output.append(f"STDOUT: {stdout}")

        if stderr:
            output.append(f"STDERR: {stderr}")

        if return_code != 0:
            output.append(f"Process exited with code {return_code}")

        if not output:
            return "No output produced."

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"

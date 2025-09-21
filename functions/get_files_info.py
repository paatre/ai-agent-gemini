import os


def get_files_info(working_directory, directory="."):
    try:
        dir_full_path = os.path.join(working_directory, directory)
        abs_work_dir = os.path.abspath(working_directory)
        abs_dir_full_path = os.path.abspath(dir_full_path)

        if not abs_dir_full_path.startswith(abs_work_dir):
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory\n"

        if not os.path.isdir(dir_full_path):
            return f"Error: \"{directory}\" is not a directory\n"

        entries = os.listdir(dir_full_path)

        file_infos = []

        for entry in entries:
            entry_full_path = os.path.join(dir_full_path, entry)
            file_size = os.path.getsize(entry_full_path)
            is_dir = os.path.isdir(entry_full_path)
            file_info = f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}"
            file_infos.append(file_info)

        return "\n".join(file_infos)

    except Exception as e:
        return f"Error: {e}\n"

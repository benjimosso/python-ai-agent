import os.path
from google.genai import types



def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(target_dir):
            raise Exception(f'Error: "{directory}" is not a directory')
        list_of_files = os.listdir(target_dir)
        final_string = []
        for l in list_of_files:
            file_path = os.path.join(target_dir, l)
            is_dir = os.path.isdir(file_path)
            file_size = os.path.getsize(file_path)
            final_string.append(f"- {l}: file_size= {file_size} bytes, is_dir={is_dir}")
        final_joined_string = " \n".join(final_string)
        print(f"Result for {directory} directory: \n{final_joined_string}")
        return f"Result for {directory} directory: \n{final_joined_string}"

    except Exception as e:
        print(e)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

import os.path
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_dir:
            raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_file):
            raise Exception(f'Error: "{file_path}" does not exist or is not a regular file')
        if not target_file.endswith('.py'):
            raise Exception(f'Error: "{file_path}" is not a Python file')
        command = ["python", target_file]
        if args:
            command.extend(args)

        sub_process_instance = subprocess.run(args=command, capture_output=True ,text=True, timeout=30, cwd=working_dir_abs)
        output_str = ""
        if sub_process_instance.returncode != 0:
            output_str = f"Process exited with code {sub_process_instance.returncode}"
        if sub_process_instance.stdout is None or sub_process_instance.stderr is None:
            output_str = "No output produced"
        elif sub_process_instance.stdout != "":
            output_str = f"STDOUT: {sub_process_instance.stdout}"
        elif sub_process_instance.stderr != "":
            output_str = f"STDERR: {sub_process_instance.stderr}"
        # print(output_str)
        return output_str



    except Exception as e:
        print(e)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            # Way to write it according to gemini api docs
            # URL: https://ai.google.dev/gemini-api/docs/function-calling?example=meeting
            # "args": {
            #     "type": "array",
            #     "items": {"type": "string"},
            #     "description":"Optional arguments to run the file."
            # }
            # the below is the way writen in bootdev solution:
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional list of arguments to pass to the Python script",
            ),

        },
        required = ["file_path"]
    ),
)
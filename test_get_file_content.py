# from functions.get_file_content import get_file_content
#
# get_file_content("calculator", "lorem.txt")
# get_file_content("calculator", "main.py")
# get_file_content("calculator", "pkg/calculator.py")
# get_file_content("calculator", "/bin/cat")
# get_file_content("calculator", "pkg/does_not_exist.py")

from functions.run_python_file import run_python_file

run_python_file("calculator", "tests.py")
import os
import argparse
from time import sleep


def project_directory_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False


def check_if_project_directory_empty(path):
    if os.listdir(path) != []:
        return False
    else:
        return True



def populate_project_directory(dir_path, name):

    subdirectories = [name, "docs", "tests"]

    def generate_license(path):
        if os.path.exists(path + "/LICENSE"):
            print("LICENSE exists")
            pass
        else:
            filename = path + "/LICENSE"
            text = """
MIT License

Copyright (c) [year] [full name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

            """
            try:
                with open(filename, "w") as f:
                    f.write(text)
                f.close()
            except:
                print("Error generating LICENSE file.")


    def generate_dir_files(path):
        files = ['/README.md', '/requirements.txt', '/test-requirements.txt', '/setup.py']
        for file in files:
            full_path = path + file
            try:
                with open(full_path, "w") as f:
                    f.write("")
                f.close()
            except:
                print("Error writing files.")

    def create_file(full_path):
        with open(full_path, "w") as f:
            f.write("")
        f.close()

    generate_license(dir_path)
    generate_dir_files(dir_path)
    for directory in subdirectories:
        full_path = "".join([dir_path, "/", directory, "/"])
        if directory in [name, "tests"]:
            try:
                os.mkdir(full_path)
                create_file(full_path + "__init__.py")
                if directory == name:
                    create_file(full_path + name + ".py")
                else:
                    create_file(full_path + "test_" + name + ".py")
            except:
                print("Error populating")
        else:
            try:
                os.mkdir(full_path)
            except:
                print("Error populating")


def main():
    """
    Generates skeleton of project based on Matt Bachmann's 2016 talk at Boston Python User Group.

    :return void:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Name of the project you are creating", type=str)
    parser.add_argument("--directory", help="Location of project. Must be an empty directory!", type=str)

    args = parser.parse_args()

    if args.directory:
        dir_path = args.directory
    else:
        dir_path = "./" + args.name


    if project_directory_exists(dir_path):
        print("Populating project directory.")
        populate_project_directory(dir_path, args.name)
    else:
        inp = input("Project directory does not exist. Would you like to create it at this time? Y/N\n")
        while inp not in ['y', 'yes', 'n', 'no']:
            inp = input("Invalid response. Try again. Please enter 'y' or 'n'.")
        if inp.lower() in ['y', 'yes']:
            os.mkdir(dir_path)
            if check_if_project_directory_empty(dir_path):
                print("Populating project directory.")
                populate_project_directory(dir_path, args.name)
            else:
                print("Project directory is not empty. Please change your parameters and try again.")
                sleep(2)
        else:
            print('Good-bye')
            sleep(2)




if __name__ == "__main__":
    main()

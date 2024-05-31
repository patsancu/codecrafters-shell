import sys
import os
import subprocess

folders = []
app_folder = os.path.dirname(os.path.realpath(__file__))
base_folder = os.sep + os.path.join(*app_folder.split(os.sep)[:-1])
home_folder = os.getenv("HOME")


def binary_exists(path, binary_name):
    for folder in path.split(":"):
        if os.path.isfile(f"{folder}/{binary_name}"):
            return folder
    return None

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #  print("Logs from your program will appear here!")
    path = os.getenv('PATH')
    available_commands = ["echo", "exit", "type", "cd", "pwd"]


    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    while True:
        exit_code = 0
        input_text = input()
        splitted = input_text.split()
        current_command = ""
        command, *rest = input_text.split()
        if command == "type":
            if len(rest) == 1:
                arg = rest[0]
                if arg in available_commands:
                    print(f"{arg} is a shell builtin")
                else:
                    binary_folder = binary_exists(path, arg)
                    if binary_folder:
                        print(f"{arg} is {binary_folder}/{arg}")
                    else:
                        print(f"{arg}: not found".removesuffix("\r"))
        elif command == "echo":
            print(" ".join(rest))
        elif command == "exit":
            if len(rest) == 1 and rest[0] == "0":
                break
            else:
                print("Exit should be used as: exit 0")
        elif command == "pwd":
            if folders:
                print(folders[-1])
            else:
                os.chdir(base_folder)
                print(base_folder)
        elif command == "cd":
            if len(rest) == 0:
                os.chdir(home_folder)
                folders.clear()
            else:
                try:
                    folder = rest[0]
                    temp_folder = []
                    if folder.startswith("."):
                        if folders:
                            current_folder = folders[-1]
                        else:
                            current_folder = base_folder
                        if folder.startswith(".."):
                            up = 0
                            for piece in folder.split(os.sep):
                                if piece == "..":
                                    up += 1
                            folder = os.sep + os.path.join(*current_folder.split(os.sep)[:-up])
                            pass
                            # going up
                        elif folder.startswith("./"):
                            # current directory
                            folder = f"{current_folder}/{folder[2:]}"
                    else:
                        if folder == "~":
                            folder = home_folder
                    os.chdir(folder)
                    folders.append(folder)
                except FileNotFoundError:
                    print(f"{folder}: No such file or directory")
        else:
            folder = binary_exists(path, command)
            if folder:
                process = subprocess.run([command, *rest])
            else:
                if os.path.isfile(command):
                    process = subprocess.run([command, *rest])
                else:
                    print(f"{input_text}: not found")
        sys.stdout.write("$ ")
        sys.stdout.flush()
    sys.exit(exit_code)



if __name__ == "__main__":
    main()

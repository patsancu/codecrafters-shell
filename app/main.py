import sys
import os
import subprocess


def binary_exists(path, binary_name):
    for folder in path.split(":"):
        if os.path.isfile(f"{folder}/{binary_name}"):
            return folder
    return None

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #  print("Logs from your program will appear here!")
    path = os.getenv('PATH')


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
                if arg in ["echo", "exit", "type"]:
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
        else:
            folder = binary_exists(path, command)
            if folder:
                process = subprocess.run([command, *rest])
            else:
                print(f"{input_text}: not found")
        sys.stdout.write("$ ")
        sys.stdout.flush()
    sys.exit(exit_code)



if __name__ == "__main__":
    main()

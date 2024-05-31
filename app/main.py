import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #  print("Logs from your program will appear here!")

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
                    print(f"{arg} not found")
        elif command == "echo":
            print(rest)
        elif command == "exit":
            if len(rest) == 1 and rest[0] == "0":
                break
            else:
                print("Exit should be used as: exit 0")
        else:
            print(f"{input_text}: not found")
        sys.stdout.write("$ ")
        sys.stdout.flush()
    sys.exit(exit_code)



if __name__ == "__main__":
    main()

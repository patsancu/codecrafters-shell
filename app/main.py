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
        if input_text.startswith("exit"):
            if len(splitted) > 1:
                arg = splitted[1]
                if arg != "0":
                    print("Argument wasn't 0!")
                    exit_code = 1
            else:
                exit_code = 2
                print("No arguments for exit")
            break
        else:
            print(f"{input_text}: not found")
        sys.stdout.write("$ ")
        sys.stdout.flush()
    sys.exit(exit_code)



if __name__ == "__main__":
    main()

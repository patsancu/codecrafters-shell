import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #  print("Logs from your program will appear here!")

    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    while True:
        input_text = input()
        print(f"{input_text}: not found")
        sys.stdout.write("$ ")
        sys.stdout.flush()


if __name__ == "__main__":
    main()

import sys

def main():
    check_argv()
    count = 0
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exits")

    for line in lines:
        count+=1
        if line.isspace() or line.lstrip().startswith("#"):
            count -= 1
    print(count)

def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2 and ".py" not in sys.argv[1] :
        sys.exit("Not a Python file")

if __name__ == '__main__':
    main()
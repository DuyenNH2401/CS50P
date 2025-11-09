import sys
import csv
import tabulate

def main():
    pizza = []
    check_argv()
    with open(sys.argv[1], mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            pizza.append(row)
    print(tabulate.tabulate(pizza[1:],headers= pizza[0], tablefmt="grid"))

def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2 and ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == '__main__':
    main()
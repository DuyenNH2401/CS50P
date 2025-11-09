import sys
import csv

def main():
    students = []
    check_argv()
    try:
        with open(sys.argv[1], mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    lname, fname = row[0].split(",")
                    lname.strip()
                    fname.strip()
                    students.append({"first":fname, "last":lname, "house":row[1]})
                except:
                    pass

        with open(sys.argv[2],mode="w", newline="") as wfile:
            writer = csv.DictWriter(wfile, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def check_argv():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3 and ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ == '__main__':
    main()

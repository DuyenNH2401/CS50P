import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^\d+\.\d+\.\d+\.\d+$"
    match = re.fullmatch(pattern, ip)
    if not match:
        return False
    numbers = ip.split(".")
    for number in numbers:
        if not (0 <= int(number) <= 255):
            return False
    return True

if __name__ == '__main__':
    main()

import re

def main():
    print(count(input("Text: ")))

def count(s):
    pattern = r"\b(um|uM|Um)+\b"
    lst = re.findall(pattern, s)
    return len(lst)

if __name__ == "__main__":
    main()
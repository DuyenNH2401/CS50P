import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"([0-2]?[0-9]):?([0-5][0-9])? (AM|PM) to ([0-2]?[0-9]):?([0-5][0-9])? (PM|AM)$"
    match = re.search(pattern, s)
    if match:
        f_h = str(match.group(1))
        f_m = str(match.group(2))
        f_time = str(match.group(3))

        if f_time == "AM" and int(f_h) == 12:
            f_h = 0
        elif f_time == "PM" and int(f_h) == 12:
            pass
        elif f_time == "PM":
            f_h = int(f_h)+12
        if f_m == "None":
            f_m = 0

        from_time = f"{int(f_h):02}:{int(f_m):02}"

        s_h = str(match.group(4))
        s_m = str(match.group(5))
        s_time = str(match.group(6))

        if s_time == "AM" and int(s_h) == 12:
            s_h = 0
        elif s_time == "PM" and int(s_h) == 12:
            pass
        elif s_time == "PM":
            s_h = int(s_h)+12

        if s_m == "None":
            s_m = 0
        to_time = f"{int(s_h):02}:{int(s_m):02}"

        if int(f_h) > 23 or int(s_h) > 23:
             raise ValueError
        return f"{from_time} to {to_time}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
import datetime
import re
import sys
import inflect

dic_of_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def main():
    try:
        date = input("Date of Birth: ")
        year, month, day = check_birth_day(date)
        birth_date = datetime.date(year, month, day)
    except:
        sys.exit("Invalid date")

    print(sing(birth_date).capitalize())


def check_birth_day(date):
    pattern = r"^[0-9]{4}-[0-1][0-9]-[0-3][0-9]$"
    if re.search(pattern, str(date)):
         return list(map(int, date.split("-")))



def sing(birth_date):
    p = inflect.engine()
    today = datetime.date.today()

    delta = (today - birth_date).days
    delta = delta*24*60
    word = p.number_to_words(delta).replace("and ","")
    return f"{word} minutes"

if __name__ == "__main__":
    main()
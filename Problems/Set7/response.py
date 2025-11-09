from validator_collection import is_email

def main():
    mail = input("What's your email address? ")
    if is_email(mail):
        print("Valid")
    else:
        print("Invalid")

if __name__ == '__main__':
    main()
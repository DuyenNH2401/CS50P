import inflect

def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            n = input("Name: ")
            names.append(n)
        except:
            break
    print(f"Adieu, adieu, to {p.join(names)}")

main()
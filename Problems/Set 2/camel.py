camel = input("camelCase: ")

for i in camel:
    if i.isupper():
        print("_" + i.lower(), end="")
    else: print(i, end="")

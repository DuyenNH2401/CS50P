name = input("What's your name? ")

file = open("Names.txt", "a")
file.write(name)
file.close()
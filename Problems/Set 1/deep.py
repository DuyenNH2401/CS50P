def main():
    prompt = input("What is the Answer to the Great Question of Life, the Universe, and Everything ")
    prompt = prompt.lower().strip()

    if prompt == "42":
        print("Yes")
    elif prompt == "forty-two":
        print("Yes")
    elif prompt == "forty two":
        print("Yes")
    else: print("No")
    print(prompt)
main()

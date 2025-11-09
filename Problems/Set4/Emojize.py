import emoji

def main():
    text = input("Input: ")
    emojize =emoji.emojize(text, language='alias')
    print(f"Output: {emojize}")

main()
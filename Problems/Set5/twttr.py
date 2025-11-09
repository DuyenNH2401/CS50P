def main():
    text = input("Input: ")
    short_txt = shorten(text)
    print(f"Output: {short_txt}")

def shorten(text):
    forb_word = ("a", "o" ,"e" ,"u" ,"i")
    short_text = ""
    for i in text:
        if i.lower() in forb_word:
            short_text += ""
        else:
            short_text +=i
    return short_text

if __name__ == "__main__":
    main()

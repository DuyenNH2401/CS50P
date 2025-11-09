from PIL import  Image, ImageOps
import sys

def main():
    check_argv()
    try:
        img = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_img = Image.open("shirt.png")
    out_img = ImageOps.fit(img, shirt_img.size)
    out_img.paste(shirt_img, shirt_img)
    out_img.save(sys.argv[2])
    img.close()
    shirt_img.close()

def check_argv():
    input_format = check_extension(sys.argv[1])
    output_format = check_extension(sys.argv[2])

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 4:
        sys.exit("Too many command-line arguments")
    elif output_format not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")
    elif input_format != output_format:
        sys.exit("Input and output have different extensions")

def check_extension(file:str)->str:
    index = file.index(".")
    return file[index:]

if __name__ == '__main__':
    main()
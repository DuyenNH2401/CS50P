from PIL import Image
from more_itertools.more import unzip

name = str(input("Name: "))
with Image.open(name) as img:
    print(img.size)

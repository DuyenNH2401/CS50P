import sys
from pyfiglet import Figlet

figlet = Figlet()
random_font = False

if len(sys.argv) == 1:
    random_font = True
if len(sys.argv) >= 2:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" or sys.argv[1] =="renders":
        pass
    else: sys.exit("Invalid Error")

if random_font:
    figlet.getFonts()
else:
    figlet.setFont(font=sys.argv[2])

word = input("Input: ")
print(figlet.renderText(word))

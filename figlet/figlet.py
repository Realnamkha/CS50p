from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    Input = input("Enter the string :")
    figlet.setFont(font = fonts[random.randint(0, 424)])
elif len(sys.argv) == 3:
    Input = input("Enter the string :")
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and (sys.argv[2] in fonts):
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid Argument")
else:
    sys.exit("Argument few or many")

print(figlet.renderText(Input))
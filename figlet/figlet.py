from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    Input = input("Enter the string :")
    if sys.argv[1] == '-f' or '--font':
        figlet.setFont(font = fonts[random.randint(0, 424)])
    else:
        sys.exit("Invalid Argument")
elif len(sys.argv) == 3:
    Input = input("Enter the string :")
    if ((sys.argv[1] == '-f' or '--font') and (argv[2] in fonts)):
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid Argument")
else:
    sys.exit("Argument few or many")

print(figlet.renderText(Input))
from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 0:
    Input = input("Enter the string :")
    figlet.setFont(font=random.choice[fonts])

elif len(sys.argv) == 2:
    Input = input("Enter the string :")
    figlet.setFont(font=argv[2])
else:
    sys.exit("Argument few or many")

print(figlet.renderText(Input))
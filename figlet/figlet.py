from pyfiglet import Figlet
import sys
Input = input("Enter the string :")
if len(sys.argv) == 0:

elif len(sys.argv) == 2:

else:
    sys.exit("Argument few or many")

print("hello, my name is", sys.argv[1])
figlet = Figlet()
print(figlet.getFonts())
figlet.setFont(font=f)
print(figlet.renderText(s))
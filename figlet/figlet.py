from pyfiglet import Figlet
import sys
if len(sys.argv) == 0:
    Input = input("Enter the string :")
    
elif len(sys.argv) == 2:
    Input = input("Enter the string :")
else:
    sys.exit("Argument few or many")

print("hello, my name is", sys.argv[1])
figlet = Figlet()
print(figlet.getFonts())
figlet.setFont(font=f)
print(figlet.renderText(s))
x = int(input("Enter the first operand"))
y = input("Enter the operand")
z = int(input("Enter the second operand"))

if (y=="+"):
    print(x+z)
elif (y=="-"):
    print(x-z)
elif (y=="*"):
    print(x*z)
else:
    print(x/z)

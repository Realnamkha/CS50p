x = int(input("Enter the first operand"))
y = input("Enter the operand")
z = int(input("Enter the second operand"))

if (y=="+"):
   print(f"{x+z:.1f}")
elif (y=="-"):
    print(f"{x-z:.1f}")
elif (y=="*"):
    print(f"{x*z:.1f}")
else:
    print(f"{x/z:.1f}")

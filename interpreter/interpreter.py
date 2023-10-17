x = int(input("Enter the first operand"))
y = input("Enter the operand")
z = int(input("Enter the second operand"))

if (y=="+"):
   w = str(x + z)
   print(f"{w:.1f}")
elif (y=="-"):
    w = str(x - z)
    print(f"{w:.1f}")
elif (y=="*"):
    w = str(x * z)
    print(f"{w:.1f}")
else:
    w = str(x / z)
    print(f"{w:.1f}")

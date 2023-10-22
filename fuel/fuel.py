try :
    X = int(input("Enter the value of X))
    Y = int(input("Enter the value of X))
except ValueError:
    print("X or Y is not an integer")
if X>Y:
    raise GreaterError()
def greater(X,Y):
    if X>Y:
        raise Exception("X is greater than Y")


try :
    X = int(input("Enter the value of X"))
    Y = int(input("Enter the value of Y"))
    greater(X,Y)
except ValueError:
    print("X or Y is not an integer")
except Exception as e:
    print(e)
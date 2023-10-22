def greater(X,Y):
    if X>Y:
        raise Exception("X is greater than Y")


try :
    X = int(input("Enter the value of X"))
    Y = int(input("Enter the value of Y"))
    greater(X,Y)
except ValueError:
    print("X or Y is not an integer")
except def check_age(age):
    if age < 18:
        raise Exception(" Age must be 18 or above. ")
    else:
        print(" Age is valid. ")   as e:
    print(e)
def main():
    X = int(input("Enter the value of X"))
    Y = int(input("Enter the value of Y"))
    
def greater(X,Y):
    if X>Y:
        raise Exception("X is greater than Y")

def get_fuel():
    while True:
        try :
            X = int(input("Enter the value of X"))
            Y = int(input("Enter the value of Y"))
            fuel = X/Y
            greater(X,Y)
            break
        except ValueError:
            print("X or Y is not an integer")
        except ZeroDivisionError:
            print("Y cannot be zero")
        except Exception as e:
            print(e)

    fuel = fuel *100
    fuel = round(fuel,1)
    return fuel
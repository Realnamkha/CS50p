def main():
    fuel = get_fuel()
    if (fuel<1):
        print("E")
    elif(fuel>99):
        print("F")
    else:
        print(f"{fuel:.0f}%")

def greater(X,Y):
    if X>Y:
        raise Exception("X is greater than Y")

def get_fuel():
    while True:
        fuel = input("Fractions: ")
        X, Y = fuel.split("/")
        print(X,Y)
        try :
            X = int(X)
            Y = int(Y)
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

main()
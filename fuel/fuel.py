def main():
    fuel = get_fuel()
    if (fuel<=1):
        print("E")
    elif(fuel>=99):
        print("F")
    else:
        print(f"{fuel:.0f}%")

def get_fuel():
    while True:
        try :
            fuel = input("Fractions: ")
            X,Y = fuel.split("/")
            X = int(X)
            Y = int(Y)
            fuel = X/Y
            if X>Y:
                raise Exception("X is greater than Y")
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
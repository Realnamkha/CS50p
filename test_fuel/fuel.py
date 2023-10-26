def main():
    fuel = get_fuel()
    percent = convert(fuel)
    gauge = 

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
    return fuel


def convert(fraction):
    fraction = fraction * 100
    fraction = round(fuel,1)
    return fraction


def gauge(percentage):
    if (percentage<=1):
        print("E")
    elif(percentage>=99):
        print("F")
    else:
        print(f"{percentage:.0f}%")


if __name__ == "__main__":
    main()
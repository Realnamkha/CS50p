def main():
    fuel = get_fuel()
    percent = convert(fuel)
    print(gauge(percent))

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
    fraction = round(fraction,1)
    return fraction


def gauge(percentage):
    if (percentage<=1):
        return "E"
    elif(percentage>=99):
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
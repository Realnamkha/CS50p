def main():
    fraction = input("Fractions: ")
    percent = convert(fraction)
    print(gauge(percent))


def convert(fraction):
    while True:
        try :
            X,Y = fraction.split("/")
            X = int(X)
            Y = int(Y)
            fraction= X/Y
            if X>Y:
                raise Exception("X is greater than Y")
            fraction = fraction *100
            fraction = round(fraction,1)
            return fraction
        except ValueError:
            print("X or Y is not an integer")
            break
        except ZeroDivisionError:
            print("Y cannot be zero")
            break
        except Exception as e:
            print(e)
            break

def gauge(percentage):
    if (percentage < 1):
        return "E"
    elif(percentage>=99):
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
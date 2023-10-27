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

            fraction = fraction * 100
            fraction = round(fraction,1)
            fraction = int(fraction)
            return fraction
        except ValueError:
            return "X or Y is not an integer"
        except ZeroDivisionError:
            return "Y cannot be zero"
        except Exception as e:
            return str(e)


def gauge(percentage):
    if (percentage < 1):
        return "E"
    elif(percentage>=99):
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
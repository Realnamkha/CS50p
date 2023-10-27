def main():
    while True:
        try:
            fraction = input("Fractions: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except ValueError:
            return "X or Y is not an integer"
        except ZeroDivisionError:
            return "Y cannot be zero"
def convert(fraction):
            X,Y = fraction.split("/")
            X = int(X)
            Y = int(Y)
            fraction= X/Y
            fraction = fraction *100
            fraction = round(fraction,1)
            return fraction

def gauge(percentage):
    if (percentage <= 1):
        return "E"
    elif(percentage>=99):
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
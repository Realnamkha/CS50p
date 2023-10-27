def main():
    while True:
        try:
            fraction = input("Fractions: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except ValueError:
            print("X or Y is not an integer")
            continue
        except ZeroDivisionError:
            print("Y cannot be zero")
            continue
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
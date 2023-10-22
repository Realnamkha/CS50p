def main():
    fuel = input("Fractions: ")
    X,Y = fuel.split("/")
    fuel = get_fuel(X,Y)
    if (fuel<1):
        print("E")
    elif(fuel>99):
        print("F")
    else:
        print(f"{fuel:.0f}%")

def greater(X,Y):
    if X>Y:
        raise Exception("X is greater than Y")

def get_fuel(input1,input2):
    while True:
        try :
            X = int(input())
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
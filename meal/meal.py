hours, minutes = input("Enter the current time ").split(":")
hours = float(hours)
minutes = float(minutes)
minutes = (minutes/60)
l = [hours,minutes]
s = '.'.join([str(n) for n in l])
print(s)
def main():
    ...


def convert(time):
    ...


if __name__ == "__main__":
    main()

def main():
    convert(new_time)


def convert(time):
    hours, minutes = input("Enter the current time ").split(":")
    hours = int(hours)
    minutes = float(minutes)
    minutes = (minutes/60)
    new_time = hours + minutes
    return new_time

if (7 <= time <= 8):
        print("Breakfast Time")
if (12 <= time <= 13):
        print("Lunch Time")
if (18 <= time <= 19):
        print("Dinner Time")
if __name__ == "__main__":
    main()
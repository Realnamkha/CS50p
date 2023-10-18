
def main():
    time = input("Enter the current time ")
    hours = convert(time)
    if (7 <= hours <= 8):
        print("Breakfast Time")
    if (12 <= hours <= 13):
        print("Lunch Time")
    if (18 <= hours <= 19):
        print("Dinner Time")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = float(minutes)
    minutes = (minutes/60)
    new_time = hours + minutes
    return new_time

if __name__ == "__main__":
    main()
from datetime import date
class Date:
 ...
def get_date():
        year,month,day = input("Enter Your DOB :").strip().split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        d = date(year, month, day)
        print(d)

def main():
    get_date()


if __name__ == "__main__":
    main()

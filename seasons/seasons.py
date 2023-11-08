from datetime import date
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def get_DOB():
        year,month,day = input("Enter Your DOB :").strip().split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        return year,month,day


    def get_today():
        year,month,day = str(date.today()).split("-")
        return year,month,day

    def __sub__(self, other):
        year = self.year + other.year
        month = self.month + other.month
        day = self.day + other.day
        return Vault(galleons, sickles, knuts)

def main():
    year,month,day = get_DOB()
    date1 = Date(year,month,day)
    year,month,day = get_today()
    date2 = Date(year,month,day)
    print(date1,date2)
if __name__ == "__main__":
    main()

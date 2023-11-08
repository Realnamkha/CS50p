from datetime import date
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @property
    def Date(self):
        return self._house
    def get_DOB():
        year,month,day = input("Enter Your DOB :").strip().split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        d = date(year, month, day)
        print(d)

    def get_today():
        today = date.today()
        print(today)

    def __sub__(self, other):
        year = self.year + other.year
        month = self.month + other.month
        day = self.day + other.day
        return Vault(galleons, sickles, knuts)


def main():
    get_DOB()
    get_today()


if __name__ == "__main__":
    main()

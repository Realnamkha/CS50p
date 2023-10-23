months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("DATE: ")
        if '/' in date:
            month,day,year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
            if (month>12 or day>31 or year<1):
                raise Exception("Out of Range")
            print(f"{year:04}-{month:02}-{day:02}")
            break
        else:
            month,year = date.split(',')
            month,day = month.split(' ')
            if month in months:
                month = months.index(month) + 1
            else:
                raise Exception("Out of Range")
            year = int(year)
            day = int(day)
            year = int(year)
            print(f"{year:04}-{month:02}-{day:02}")
            break
    except ValueError:
        print("ValueError has occureed")
    except Exception as e:
        print(e)
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
try:
    date = input("DATE: ")
    if '/' in date:
        month,day,year = date.split('/')
        month = int(month)
        day = int(day)
        year = int(year)
        if(month>12 or day>31 or year<1):
            raise Exception("Format is incorrect")
    else:
        month,year = date.split(',')
        month,day = month.split(' ')
        if month in months:
             month = months.index(month)
        year = int(year)
        day = int(day)
        year = int(year)
except ValueError():
    print("ValueError has occrued")
finally:
        print(f"{year:04}-{month:02}-{day:02}")
[
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
        print(f"{year:04}-{month:02}-{day:02}")
        if(month>12 or day>31 or year<1):
            raise Exception("Format is incorrect")
    else:
        month,year = date.split(',')
        day,month = month.split(' ')
except ValueError():
    print("ValueError has occrued")
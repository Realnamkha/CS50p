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

date = input("DATE: ")
if '/' in date:
    month,day,year = date.split('/')
    print(f"{year:04}-{month:02}-{day:02}")
    if(int(month)>12 or int(day)>31 or int(year)<1):
        raise Exception("Format is incorrect")
else:
    month,year = date.split(',')
    day,month = month.split(' ')

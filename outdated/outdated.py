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
if date.contains('/'):
    month,day,year = date.split('/')
    if(int(month)>12 or int(day)>31 or int(year)<1):
        raise Exception("Format is incorrect")
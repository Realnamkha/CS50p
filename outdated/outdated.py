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
month,day,year = date.split('/')
if(month>12 or day>31 or year<1):
    raise Exception(")
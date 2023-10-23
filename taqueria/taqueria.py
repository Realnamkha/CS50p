import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),s)

items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
while True:
    total = 0
        try:
            food = input("Food: ")
        except EOFError:
            print("PROGRAM EXIT")
        else:
            food = titlecase(food)
            for item in items:
                if (food == item):
                total += items[item]
                print(f"Total: ${total:.2f}")
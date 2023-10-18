camelCase = input("Enter the variable ").strip()
snake_case = ""
def convert(camelCase):
    for i in range(len(camelCase)):
        if (camelCase[i].isupper()):
            smoke_case += "_" + camelCase[i].lower()
        else:
            smoke_case += camelCase[i].lower()
    return smoke_case
convert(camelCase)
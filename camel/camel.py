camelCase = input("Enter the variable ").strip()
def convert(camelCase):
    for i in range(len(camelCase)):
        if (camelCase[i].isupper()):
            smoke_case += "_" + camelCase[i].lower()
        else:
            smoke_case += camelCase[i].lower()

    return smoke_case
print(convert(camelCase))
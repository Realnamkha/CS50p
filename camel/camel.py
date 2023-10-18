camelCase = input("Enter the variable ").strip()
snake_case = ""

def convert(camelCase):
    for i in range(len(camelCase)):
        if camelCase[i].isupper():
            snake_case += "_" + camelCase[i].lower()
        else:
            snake_case += camelCase[i].lower()
    return snake_case

snake_case = convert(camelCase)
print("Snake case:", snake_case)


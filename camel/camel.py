camelCase = input("Enter the variable ").strip()

def convert(camelCase):
    snake_case = ""
    for i in range(len(camelCase)):
        if camelCase[i].isupper():
            snake_case += "_" + camelCase[i].lower()
        else:
            snake_case += camelCase[i].lower()
    return snake_case

snake_case = convert(camelCase)
print("Snake case:", snake_case)


camelCase = input("Enter the variable ").strip()
for i in range(len(camelCase)):
    if (camelCase[i] == camelCase[i].isupper()):
        print(camelCase[i])
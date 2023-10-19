string = input("Enter the string ").strip().lower()
vowels = ['a','e','i','o','u']
for char in string:
    new_string = ""
    if char not in vowels:
        new_string +=char
print(new_string)

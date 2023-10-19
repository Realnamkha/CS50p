string = input("Enter the string ").strip().lower()
vowels = ['a','e','i','o','u']
new_string = ""
if string not in vowels:
    new_string +=string

Greetings = input("Enter your greetings").lower().strip()
if Greetings.startswith("Hello"):
    print("$0")
elif Greetings.startswith("H"):
    print("$20")
else:
    print("$100")
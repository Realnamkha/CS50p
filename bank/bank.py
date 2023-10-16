Greetings = input("Enter your greetings").lower().strip()
if Greetings.startswith("hello"):
    print("$0")
elif Greetings.startswith("h"):
    print("$20")
else:
    print("$100")
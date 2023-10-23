items = []
while True:
        try:
              items += input().split("/n")
        except EOFError:
            print("PROGRAM EXIT")
            break

print(items)
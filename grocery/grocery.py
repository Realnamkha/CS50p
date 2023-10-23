def remove_duplicates(x):
  return list(dict.fromkeys(x))

items = []
while True:
        try:
              items += input().upper().split("/n")
        except EOFError:
            print("PROGRAM EXIT")
            break

items.sort()
for item in items:
      count = items.count(item)
      print(f"{count} {item}")
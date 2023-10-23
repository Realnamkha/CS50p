from collections import Counter
items = []
while True:
        try:
              items += input().upper().split("/n")
        except EOFError:
            print("PROGRAM EXIT")
            break

items.sort()
item_counts = Counter(items)

unique_items = list(item_counts.keys())

for item in unique_items:
    count = item_counts[item]
    print(f"{count} {item}")
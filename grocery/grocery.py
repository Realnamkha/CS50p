while True:
        try:
              items += input().split()
              for item in items:
                print(item)
        except EOFError:
            print("PROGRAM EXIT")
            break
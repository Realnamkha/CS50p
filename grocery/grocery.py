while True:
        try:
              item = input().split()
              print(item)
        except EOFError:
            print("PROGRAM EXIT")
            break
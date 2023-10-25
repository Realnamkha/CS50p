import sys
while True:
    try:
        n = float(sys.argv[1])
        break
    except ValueError:
        sys.exit("Input is not a number")
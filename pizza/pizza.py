import sys
try:
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        if (file_name[-4:] == ".csv"):
            with open(file_name) as file:
                lines = file.readlines()
                for line in lines:
                    if ((line.strip().startswith("#")) or  (line.strip() == "")):
                        pass
                    else:
                        count +=1
                print(count)

        else:
            sys.exit("Not a Python file")
    else:
        sys.exit("More or few arguments")
except FileNotFoundError:
    sys.exit("File does not exist")

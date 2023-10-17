fileinput = input("Enter the file name with extension").lower().strip()
if ".gif" in fileinput:
    print("image/gif")

elif (".jpg" or "jpeg") in fileinput:
    print("image/jpeg")

elif ".png" in fileinput:
    print("image/png")

elif ".pdf" in fileinput:
    print("application/pdf")

elif ".txt" in fileinput:
    print("image/txt")

elif ".zip" in fileinput:
    print("image/zip")
else:
     print("application/octet-stream")
fileinput = input("Enter the file name with extension").lower().strip()
if ".gif" in fileinput:
    print("image/gif")

elif ".jpg" in fileinput:
    print("image/jpeg")

elif "jpeg" in fileinput:
    print("image/jpeg")

elif ".png" in fileinput:
    print("image/png")

elif ".pdf" in fileinput:
    print("application/pdf")

elif ".txt" in fileinput:
    print("text/plain")

elif ".zip" in fileinput:
    print("application/zip")
else:
     print("application/octet-stream")
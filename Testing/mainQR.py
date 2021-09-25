from tools import generatenewQR, checkqrcode, extractxl


#We will get this name list from excel or a text file
nameList = extractxl()

print("Welcome to QR Interface 0.1")
userInput = int(input("If you would to create qr codes please press 1\nIf you would like to check if a QR exists please press 2\n"))

if userInput == 1:
   generatenewQR(nameList)

elif userInput == 2:
   img = input("Please enter QR image name with extension\neg: dog.py\n")
   checkqrcode(img)

else:
    print("Invalid Input")
    quit()
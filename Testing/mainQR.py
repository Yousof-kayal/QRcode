from tools import generateQR, readqrcode



#We will get this name list from excel or a text file
nameList = ['Aamer','Yousof',"Mostafa","Adnan","Abook","OMMAK","Jeddak"]

print("Welcome to QR Interface 0.1")
userInput = int(input("If you would to create qr codes please press 1\nIf you would like to scan a QR please press 2\n"))

if userInput == 1:
    generateQR(nameList)
elif userInput == 2:
   img = input("Please enter QR image name with extension\neg: dog.py\n")
   print(f"The QR code that has been scanned is {readqrcode(img)}")

else:
    print("Invalid Input")
    quit()
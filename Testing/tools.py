import random
import string
import pyqrcode
import png
import pyzbar
from PIL import Image
from pyzbar.pyzbar import decode
import sqlite3


#Function to create qr codes

def createqr(keylist, nameList):
    connection = sqlite3.connect('inviteeslist.db')
    length = len(nameList)
    for j in range(length):
        QR = pyqrcode.create(f"{keylist[j]}")
        QR.png(f'{keylist[j]}.png', scale=8)
        connection.execute(f"INSERT INTO INVITEES (CODE,NAME) VALUES ('{keylist[j]}','{nameList[j]}')")

    connection.commit()
    connection.close()




#Function to read a QR code and return a value



def readqrcode(imageName):
    from pyzbar.pyzbar import decode
    data = decode(Image.open(imageName))
    for i in data:
        return ((i.data.decode("utf-8")))



def generateQR(nameList):
    """
    Prompting user to select number of QR codes to generate,
    the value entered reflects the number of loops.
    As well as the length of the QR code.
    """

    # QRamount = int(input("How many QR codes would you like to generate?"))
    # QRlength = int(input("How long should each QR string be?"))
    QRlength = 10

    """Making a list with a specified amount of random integers"""
    keylist = []
    for i in range(len(nameList)):
        QRrandom = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(QRlength))
        keylist.append(QRrandom)

    """
    Here is the QR code generator function.
    It creates elements incrementally from the list (keylist)
    """
    createqr(keylist,nameList)

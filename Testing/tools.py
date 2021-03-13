import random
import string
import pyqrcode
import png
import pyzbar
from PIL import Image
from pyzbar.pyzbar import decode
import sqlite3
import pandas



#Function to create qr codes

def createqr(keylist, nameList):
    connection = sqlite3.connect('inviteeslist.db')
    length = len(nameList)
    connection.execute("DELETE FROM invitees")
    for j in range(length):
        QR = pyqrcode.create(f"{keylist[j]}")
        QR.png(f'{keylist[j]}.png', scale=8)
        connection.execute(f"INSERT OR REPLACE INTO INVITEES (CODE,NAME) VALUES ('{keylist[j]}','{nameList[j]}')")

    connection.commit()
    connection.close()



#Function to read a QR code and return a value


def readqrcode(imageName):
    data = decode(Image.open(imageName))
    for i in data:
        return ((i.data.decode("utf-8")))



def checkqrcode(imageName):
    bad_char = ['(', ')', ","]
    connection = sqlite3.connect('inviteeslist.db')
    cur = connection.cursor()
    input = readqrcode(imageName)
    cur.execute(f"SELECT name from invitees where code like '%{input}%'")
    data = str(cur.fetchone())

    for i in bad_char :
        data = data.replace(i, '')

    if not data:
        print("User not found")
    else:
        print(f"User {data} has been found")

    connection.close()



def generatenewQR(nameList):
    """
    Prompting user to select number of QR codes to generate,
    the value entered reflects the number of loops.
    As well as the length of the QR code.
    """

#    QRlength = int(input("How long should each QR string be?"))
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

def extractxl():
  test = pandas.read_excel(r'C:\Users\yoyo8\Desktop\QRcode\Data\namesheet.xlsx')
  namelist = test["Name"].tolist()
  return namelist


# def downloadqr():
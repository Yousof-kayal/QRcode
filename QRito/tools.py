import random
import string
import pyqrcode
import png
import pyzbar
import hashlib
from PIL import Image
from pyzbar.pyzbar import decode
import sqlite3
import pandas



"""
This connects to the database, and adds the key and name pairs to the it.
"""
def createdataentry(keylist, nameList):
    connection = sqlite3.connect('C:/Users/yoyo8/OneDrive/Desktop/QRcodeProject/Data/inviteeslist.db')
    length = len(nameList)
    connection.execute("DELETE FROM invitees")
    for j in range(length):
        QR = pyqrcode.create(f"{keylist[j]}")
        QR.png(f'C:/Users/yoyo8/OneDrive/Desktop/QRcodeProject/QRimg/{keylist[j]}.png', scale=8)
        connection.execute(f"INSERT OR REPLACE INTO INVITEES (CODE,NAME) VALUES ('{keylist[j]}','{nameList[j]}')")

    connection.commit()
    connection.close()


"""
This allows for adding names from an excel sheet found in the Data folder
"""
def readqrcode(imageName):
    data = decode(Image.open(imageName))
    for i in data:
        return ((i.data.decode("utf-8")))


"""
This accesses the database (inviteeslist),
and prints the scanned QR's corresponding name
"""
def checkqrcode(imageName):
    bad_char = ['(', ')', ","]
    connection = sqlite3.connect('C:/Users/yoyo8/OneDrive/Desktop/QRcodeProject/Data/inviteeslist.db')
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


"""
This creates random strings and incrementally adds to list (keylist)
"""
def generatenewQR(nameList):
#    QRlength = int(input("How long should each QR string be?"))
    QRlength = 32

    """Making a list with a specified amount of random integers"""
    keylist = []
    for i in range(len(nameList)):
        QRrandom = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(QRlength))
        keylist.append(QRrandom)

    createdataentry(keylist,nameList)


"""
This allows for adding names from an excel sheet found in the Data folder
"""
def extractxl():
  test = pandas.read_excel(r'C:\Users\yoyo8\OneDrive\Desktop\QRcodeProject\Data\namesheet.xlsx')
  namelist = test["Name"].tolist()
  return namelist


# def downloadqr():
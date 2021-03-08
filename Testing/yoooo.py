import random
import string
import pyqrcode

"""
Prompting user to select number of QR codes to generate,
the value entered reflects the number of loops.
As well as the length of the QR code.
"""

QRamount = int(input("How many QR codes would you like to generate?"))


QRlength = int(input("How long should each QR string be?"))


"""Making a list with a specified amount of random integers"""
keylist = []
for i in range(0,QRamount):
    QRrandom = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(QRlength))
    keylist.append(QRrandom)

"""
Here is the QR code generator function.
It creates elements incrementally from the list (keylist)
"""
def createqr():
     for j in range(0,QRamount):
      QR = pyqrcode.create(f"{keylist[j]}")
      QR.png(f'{keylist[j]}.png', scale=8)
#      QR.eps(f"{keylist[j]}.eps", scale=2)
#      print(QR.terminal(quiet_zone=1))

createqr()


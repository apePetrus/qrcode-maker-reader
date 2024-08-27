import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


def makeImg():
    msg = input('Write a message to make a QRCode: \n')

    img = qrcode.make(msg)
    img.save('output.png')


def readImg():
    msg = input('Write the QR Code\'s file name: \n')

    img = Image.open(msg)
    result = decode(img)

    print(result)

def choose():
    choice = int(input('Select an option, (1) make a QRcode or (2) read a QRcode: '))

    try:
        if choice == 1:
            makeImg()
        elif choice == 2:
            readImg()
    except:
        choose()

choose()
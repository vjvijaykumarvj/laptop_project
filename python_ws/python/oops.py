import pyqrcode
#string Which Represent The QR Code
s='www.http://127.0.0.1:8000/contactus/.com'
#generate QR Code
url = pyqrcode.create(s)
#Create And Save The svg file naming "myqt.svg"
url.svg('myqr.svg',scale=8)
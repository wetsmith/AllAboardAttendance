from django.shortcuts import render

# Create your views here.

'''
Gets an input URL(now just temp url), creates a QR code from it.

Needs to install pillow
"pip install qrcode[pil]" command will do it in your virtual environment

For further modifications, please refer to: https://pypi.org/project/qrcode/

'''

import qrcode
import string
import random


#have to add url fetching functionality(Getting url from somewhere else)
chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
url = "testabc"
qrname = ''.join(random.choice(chars) for _ in range(10))

#generate qr code for it
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

#saves generated QR code into images directory
#can be modified like sending this image to somewhere else.
img = qr.make_image()
img_name = "images/"+qrname+".png"
img.save(img_name)
qr.clear()


#!/usr/bin/env python3

import qrcode
import sys

input_data = "https://www.google.com"

qr = qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('output.png')

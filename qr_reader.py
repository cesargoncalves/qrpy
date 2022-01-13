#!/usr/bin/env python3

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('input.png')
result = decode(img)
for i in result:
    print(i.data.decode("utf-8"))

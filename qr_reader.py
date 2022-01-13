import cv2
import numpy as np

## input image is input.png
inputImage = cv2.imread("input.png")

## detect and decode the qrcode
decoder = cv2.QRCodeDetector()
data = decoder.detectAndDecode(inputImage)[0]

## show data
if len(data)>0:
  print(format(data))
else:
  print("QR Code not detected")

import numpy as np
from pyzbar.pyzbar import decode
import cv2
from PIL import Image, ImageEnhance




#img = cv2.imread('newImage.jpg')

cap = cv2.VideoCapture(0)
#if not (cap.isOpened()):
#    print('Could not open video device')
cap.set(3,640)
cap.set(4,480)

while True:
    success,img = cap.read()
# print(decode(img))
    for barcode in decode(img):
        print(barcode.data.decode('utf-8'))
cv2.imshow('Result',img)
cv2.waitKey(1)


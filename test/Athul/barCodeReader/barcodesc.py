import numpy as np
from pyzbar.pyzbar import decode
import cv2
from PIL import Image, ImageEnhance

'''im = Image.open("bara.jpg")
enhancer = ImageEnhance.Sharpness(im)
enhanced_im = enhancer.enhance(50.0)
enhanced_im.save("enha.jpg")'''
br = False
for i in range(20,256,5):
    for j in range(0,121,5):
        for k in range(0,121,5):
            black = (0, 0, 0)
            white = (255, 255, 255)
            threshold = (i, j, k)
            print(threshold)

            # Open input image in grayscale mode and get its pixels.
            img = Image.open("brct.jpg").convert("LA")
            pixels = img.getdata()

            newPixels = []

            # Compare each pixel
            for pixel in pixels:
                if pixel < threshold:
                    newPixels.append(black)
                else:
                    newPixels.append(white)

            # Create and save new image.
            newImg = Image.new("RGB", img.size)
            newImg.putdata(newPixels)
            newImg.save("newImage.jpg")

            img = cv2.imread('newImage.jpg')

            '''cap = cv2.VideoCapture(0)
            #if not (cap.isOpened()):
            #    print('Could not open video device')
            cap.set(3,640)
            cap.set(4,480)'''

            '''while True:
                success,img = cap.read()'''
            # print(decode(img))
            for barcode in decode(img):
                rollno = barcode.data.decode('utf-8')
                if (rollno == "1602-19-735-071"):
                    br = True
                    print("Success")
            # cv2.imshow('Result',img)
            # cv2.waitKey(1)
            if br:
                break
        if br:
            break
    if br:
        break

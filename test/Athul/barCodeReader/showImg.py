#from PIL import Image

#read the image
#im = Image.open("brct.jpg")

#show image
#im.show()

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('brct.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as pd
img =cv2.imread('lena.png')

smaller =cv2.pyrDown(img)#pyr up and down function to image pixls is creted
Larger  =cv2.pyrUp(img)

cv2.imshow('Original',img)#Real image or original img
cv2.imshow('Smaller',smaller)#Image is half of the real img   ofe qual
cv2.imshow('Larger',larger) # Original image is double times of larger img.

cv2.waitKey(0)
cv2.destroyAllWindows()
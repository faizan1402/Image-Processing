import cv2
import numpy as np
img =cv2.imread("lena.png")

cv2.imshow("Original Image",img)

cv2.waitKey(0)
#M=np.ones(img.shape,dtype ="uint8")*150 #means 150 to multiply and pixels are exceed

M1=np.zeros(img.shape,dtype="uint8")+150 #beacuse during multiply value is always zero

added =cv2.add(img,M1) #pixle  is increase the  pixl the original  pixel
cv2.imshow("Added",added)#and show the image and img is bright form

subtracted =cv2.subtract(img,M1)# Pixle is decrease the original pixel
cv2.imshow('Subtract',subtracted)#img is dull form pixel is decrese the original pixel
 
mult =cv2.multiply(img,M1) #and original pixel to exceed the original pixel
cv2.imshow('multiply',mult)#img is exceed  position and all pixel is exceed position is recieved

cv2.waitKey(0)
cv2.destroyAllWindows()


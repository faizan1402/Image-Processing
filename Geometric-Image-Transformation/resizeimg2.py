import cv2 
import numpy as pd
import cv2
import  numpy as pd
img =cv2.imread("lena.png")

cv2.imshow("Original image",img)
cv2.waitKey(0)

#Let's make the size of our image 3/4 of it;s original size
img_scaled =cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow('Scaling-Linear Interpoltation',img_scaled)
#scaling is  the lenear image
cv2.waitKey()

#Let's doubled th size of our image

img_scaled1=cv2.resize(img,None,fx =2,fy=2,interpolation =cv2.INTER_CUBIC)
#Cubic Interpolation is the image is very large  as compair the original img
cv2.imshow('Scaling-Cubic Interpolatation',img_scaled1)
cv2.waitKey()

#Let's skew the re-sizing by setting exact dimensions
img_scaled2 =cv2.resize(img,(900,400),interpolation=cv2.INTER_AREA)
cv2.waitKey()

cv2.destroyAllWindows()


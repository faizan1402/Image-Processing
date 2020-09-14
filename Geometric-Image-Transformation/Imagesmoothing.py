# image Blurring 
import cv2
import numpy as np

img=cv2.imread("lena.png")
cv2.imshow("Original Image",img)

cv2.waitKey(0)

# Averaging done by convolving the image with a normalize box filter
# This takes the pixels under the  box and replce th ecentral element
# max size needs to odd positive 
blur =cv2.blur(img,(20,20)) #menas height and weidth form image is blur
# blur function through img smooth or blur
#so blur function is used or 2Dfilter also used so either kernel matirx
cv2.imshow("Blur Image",blur)
cv2.waitKey(0)

cv2.destroyAllWindows()

#Instead of using Box filter use gaussinon kernel
#GaussianBlur function 
#Gausian is a light weight and blur is better form and also smoothing better form
 
Gaussian =cv2.GaussianBlur(img,(7,7),0) 
cv2.imshow('Gaussian Blur Image',Gaussian)
cv2.waitKey(0)

#Take median of all the pixels under Kernel area and central
#element is replaced with this median value 
# median blur is the only pixel is smooth and min blur can come
#MedianBlur is a heavy function and high quality processor use then you can run
#other wise problem is phase 


#median =cv2.medianBlur(img,5)
#cv2.imshow('Median Blur Images',median)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

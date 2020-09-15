'''
1-Edge detection means shape edge detect
2-the gradient represents the slope of the tangent of the graph of the function. More precisely,
 the gradient points in the
menas edge detect the only when x axis width of pixels is detect
and y is the height of pixel is detect 

'''




import cv2
import numpy as np
img=cv2.imread("lena.png",0)

height,width =img.shape
# sobel is very noise effect and clear is not detect the pixls

#Extract slop edges (sobel is the old  function detect)
#So detect the edge using sobel function sobel_x = cv.sobel(img,cv2.CV(64 bit float value,width of x, size ,k(kernel size ))
sobel_x= cv2.Sobel(img,cv2.CV_64F,1, 0, ksize =1)
# sobel_y is height value is show y is the height of value

sobel_y = cv2.Sobel(img,cv2.CV_64F,0, 1, ksize =1)

cv2.imshow("Original Image",img)
cv2.waitKey(0)

cv2.imshow('Sobel X Image',sobel_x)
cv2.waitKey(0)

cv2.imshow('Sobel Y Image',sobel_y)
cv2.waitKey(0)
sobel_Or =cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow("Sobel or Image",sobel_Or)
cv2.waitKey(0)

#Laplacian function used  image edge detect the pixels

laplacian =cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("Laplacian Image",laplacian)
cv2.waitKey(0)
#Laplacian function 
'''Canny Edge detection uses gradiant values as two  thresholds value is detect
canny=cv2.Canny(img,20,170)
Canny is very much image edge pixel detect very easily and very imp function to used the pixels
 And depends on threshold value and canny edge sufficent image edge detect the pixle
 and clear the pixel detect very good form
 And noise very reduce the canny edge detect 
 and thereshold w

''' 
canny=cv2.Canny(img,20,170)
cv2.imshow('Canny Edge',canny)

cv2.waitKey(0)


cv2.destroyAllWindows()




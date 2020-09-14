import cv2
import numpy as np

img =cv2.imread("messi5.jpg")
img2 =cv2.imread("lena.png")

print(img.shape)# returns a tuple of numbers of rows ,coloumns,and channels
print(img.size) #returns Total number of pixels is accessed
print(img.dtype)#returns Image data type is obtained

b,g,r =cv2.split(img)# means three parts of image split
img =cv2.merge((b,g,r))#merge bgr color inside img
#ROI-Region of interest means player want to corner of the right side
#ball =img[280:340 ,330 :390]   #img[left hand side upper corner :right hand side lower corner]
#img[273:333,100:160] = ball

img =cv2.resize(img ,(512,512))#rigion of center selected means
img2 =cv2.resize(img2,(512,512))

#dst =cv2.add(img,img2);# Means merge(overlapping)  the image messi5 img and lena img both are merge
dst =cv2.addWeighted(img,.9, img2, .3 ,.3);#this  function basically img weighted (img1 (src1),alpha,img2(src2),beta,gamma,dst)->None

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#  (280, 450, 3) size print (row,coloumn,channel)
#378000 shape print
#uint8 data type
#Python: cv.AddWeighted(src1, alpha, src2, beta, gamma, dst) → None

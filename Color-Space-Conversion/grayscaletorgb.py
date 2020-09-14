import cv2
img =cv2.imread('lena.png')

cv2.imshow('IMAGE',img)

cv2.waitKey(0)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Means BGR2GRAY (color) to Gray img(black and white img) 

cv2.imshow("Gray scale Image", gray_img)

cv2.waitKey(0)

cv2.destroyAllwindows()   
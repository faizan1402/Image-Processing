#How to convert RGB to HSV color (H=Hue means all color show the image)
# (S=Saturation saturation means any particular color)
# (V=Value means intensity low to high intensity)
#Color filter and color space
#HUe =0 to 180 ,Saturation = 0 to 255 ,Value = 0 to 255
#Hue channel  is the combination of black and white
# Value channel is only grayscale img form 
#Saturation img is the exray image form
import cv2

img= cv2.imread("lena.png")

img_HSV =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image",img_HSV)
 
cv2.imshow('Hue channel',img_HSV[:,:,0])
cv2.imshow('Saturation',img_HSV[:,:,1])
cv2.imshow('Value Channel',img_HSV[:,:,2])

cv2.waitKey(0)
cv2.destroyAllwindows()
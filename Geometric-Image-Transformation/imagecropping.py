#image Cropping
import cv2
import numpy as pd

img =cv2.imread("lena.png")

height,width =img.shape[:2] #basically height and width form extract image
#
#Means height and width cropp the img and 25% is height and 25% is width is extract 
start_row,start_col =int(height*.25),int (width*.25)
#When before the img starting value and ending value cropp

#Means 100 % to 25 % is starting value is and endng value is 75% remaining
end_row,end_col =int(height*.75),int(width*.75)
# using cropped function and 25 % is cropp the img and remaining is the simple img
cropped =img[start_row:end_row,start_col:end_col]


cv2.imshow("Oringinal",img)
cv2.waitKey(0)

cv2.imshow("cropped",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

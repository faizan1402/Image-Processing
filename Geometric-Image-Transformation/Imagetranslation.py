import cv2
import numpy as np
img =cv2.imread('faizan.jpg')

# Stroe height and width of the image
height ,width =img.shape[:2]
# shape is function and print height and width o to 2 index value  
print(height)
print(width)

# It means original img devide by any form ,How much img u re see
#And quarter is a function which devide height and width form
quarter_height ,quarter_width =height/400,width/100
print(quarter_height)
print(quarter_width)

#Translation the image Either left to right or right to left image rotate
# T is our translation Matrix
# [1,o,Tx] Tx= width of pixel x axis
#[0,1Ty ] Ty= height of pixel y axis 
T=np.float32([[1,0,quarter_width],[0,1,quarter_height]])
#means '0' and '1' tanslation image of pixels

print(T)
#We use warpAffine Translation to shift the image
#WarpAffine is width and height both are parallel to each other And  shape is lenaer form
#WarpAffine is height and width of parallel pixls form
#NonWarpAffiene basically shape is some different or non lenear shape


img_translation =cv2.warpAffine(img,T,(width,height))
cv2.imshow('Original Image',img)
cv2.imshow('Translation Image',img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
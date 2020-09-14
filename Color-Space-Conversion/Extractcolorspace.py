import cv2
import numpy as np

img =cv2.imread('lena.png')

cv2.imshow("Original Image",img)

cv2.waitKey(0)

B,G,R =cv2.split(img)
#RGB is the reverse of BGR 
zeros=np.zeros(img.shape[:2],dtype="uint8")
#np (numpy library and (zero matrix create and unsignint 8)
#original shape of three img of size same size of image is create

cv2.imshow("BLUE",cv2.merge([B,zeros,zeros]))
#merge function  through imge extract and and different plane of image show 

cv2.waitKey(0)

cv2.imshow("GREEN",cv2.merge([zeros,G,zeros]))

cv2.waitKey(0)

cv2.imshow("RED",cv2.merge([zeros,zeros,R]))

cv2.waitKey(0)

cv2.destroyAllWindows() 


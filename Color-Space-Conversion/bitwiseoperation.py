import cv2
import numpy as np

img1 =np.zeros((250,500,3),np. uint8)# this is the black color background print
img1 =cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)#cv.rectangle(img1,(rectangle is black color ,rectangle is black white color),-1 (thickness is whole color filed))

img2 =cv2.imread("messi5.jpg")
#bitAnd=cv2.bitwise_and(img2,img1) #pixels value print and two block create and black and white img show 
#bitor=cv2.bitwise_or(img2,img1) # means 'or' operator when '0' is black pixl and '1' is white pixl
bitX 

cv2.imshow("img1",img1) #print whitrectangele  
cv2.imshow("img2",img2)

#cv2.imshow('bitAnd',bitAnd)
cv2.imshow('bitAnd',bitor)

cv2.waitKey(0)
cv2.destroyAllWindows()

#  out put - Some black area and some white area
#Bitwise operation and  using mask operation binary image pixls load 
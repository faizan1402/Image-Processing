import cv2 as cv
import numpy as np

img =cv2.imread("g radient.jpg",0)
th1 =cv2.threwshold(img,50,255,cv2.THRESH_BINARY)
th2 =cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
th3 =cv2.threshold(img,255,cv2.THRESH_TRUNC)
th4 =cv2.threshold(img,255,cv2.THRESH_TOZERO)
th5 =cv2.threshold(img,255,cv2_THRESH_TOZERO_INV)


cv2.imshow("Image",img)
cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.imshow("th4",th4)
cv2.imshow("th5",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()  
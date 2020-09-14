  # How to convert Grayscale imgage to binary image 
 # binary img black pixl is '0' and white pixl is '1'

import cv2

img =cv2.imread("lena.png",0)


cv2.imshow("Gray scale",img)

cv2.waitKey(0)


 #black and white =threshold (thereshold,maximu_value,type)

ret, bw =cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow("Binary image",bw)

cv2.imwrite("Copy_Binary Image.png",bw)

cv2.waitKey(0)

cv2.destroyAllWindows()
  

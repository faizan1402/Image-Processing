import cv2
import numpy as np

from matplotlib import pyplot as plt

img =cv2.imread("circlesdetect.png",cv2.IMREAD_GRAYSCALE)
#mask detect the image and convert the binary image 
_,mask =cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernal =np.ones((1,1),np.uint8) #size of dot increases inside black dot  suppose (5,5) then increases the size of dot value increases
#How to use dilation for remove the detect the black dot 

dilation =cv2.dilate(mask,kernal,iterations=2) #iterations means the remove the blacks dots

#How to use erosion erosion added the black dot
erosion =cv2.erode(mask,kernal,iterations=1)
# how to used opening function	
opening =cv2.marphologyEx(mask,cv2.MORPH_OPEN,kernal)
titles =['mask','diation','erosions','opening']
images =[img,mask,dilation,erosion,odeninfg


for i in range(5):#means loop 2 times run  first is grayscale and second is binary image
	plt.subplot(2,3,i+1),plt.imshow(images[i] ,'gray')#size of any value increases the 
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()






'''- Morphological transformations are some simple operations based on the image shape.
Morphological performs binary numbers.
-A kernel tells you how to change the value of any given pixel by combining it with differnt amounts
 of the neightboring pixels.

 Using matplotlib library  and gray scale image
Out put - Original grayscale image ,mask detect the image (convert binary image) and dilation to remove the black dot inside mask
and dilation variable to remove the dot .
When errosin value icreaes then size of black dot decrese when iterations value increase then img is decrease pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
'''


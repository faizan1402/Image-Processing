''' The canny edge detector is an edge detection operator that uses a multi algortihm to
 detect a wide  range of edges in images. it was developed by john F.canny in 1986.


    The canny edge detecion algorithm is composed of 5 steps :
    1 Noise redution 
    2 Gradient calculation 
    3 Non- maximum suppression 
    4 Double threshold
     5 Edge tracking by hysteresis '''

import cv2 
import numpy as np
from matplotlib import pyplot as plt 
img  =cv2.imread('messi5.jpg',1)# zero means gray scale image and 1 is color image 

# How to used canny function 
canny =cv2.Canny(img,100,200)#Left to right threshold value is 

titles =['image','canny'] #added to the list 
images =[img,canny] #images list added 

for i in range(2):
  	plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')#1 by 2 images show 
  	plt.title(titles[i]) #titles means heading the titles
  	plt.xticks([]) ,plt.yticks([ ])#

plt.show()

''' The canny edge detector is an edge detection operator that uses a multi algortihm to
 detect a wide  range of edges in images. it was developed by john F.canny in 1986.


    The canny edge detecion algorithm is composed of 5 steps :
    1 Noise redution 
    2 Gradient calculation 
    3 Non- maximum suppression 
    4 Double threshold
     5 Edge tracking by hysteresis'''

import cv2 
import numpy as np
from matplotlib import pyplot as plt 
img  =cv2.imread('messi5.jpg',0)
titles =['image']
images =[img]

for i in range(1):
  	plt.subplot(1,1,i+1),plt.imshow(images[i],'gray')
  	plt.title(titles[i])
  	plt.xticks([],plt.yticks([ ]))
plt.show()

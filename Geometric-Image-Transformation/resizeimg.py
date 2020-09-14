#OpenCV Resize image using cv2.resize()

 
#Resizing an image means changing the dimensions of it, be it width alone, height alone or both. Also, the aspect ratio of the original image could be preserved in the resized image. To resize an image, OpenCV provides cv2.resize() function.

#In this tutorial, we shall the syntax of cv2.resize and get hands-on with examples provided for most of the scenarios encountered in regular usage.

#OpenCV Python – Resize image
#Syntax of cv2.resize()
#Following is the syntax of resize function in OpenCV:

#cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
#The description about the parameters of resize function.

#Parameter	Description
#src	[required] source/input image
#dsize	[required] desired size for the output image
#fx	[optional] scale factor along the horizontal axis
#fy	[optional] scale factor along the vertical axis
#interpolation	[optional] flag that takes one of the following methods. INTER_NEAREST – a nearest-neighbor interpolation 

 #a Lanczos interpolation over 8×8 pixel neighborhood
 #it is similar to the INTER_NEAREST method. INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood INTER_LANCZOS4 –
 #INTER_LINEAR – a bilinear interpolation (used by default) INTER_AREA – 
  #It may be a preferred method for image decimat

# resampling using pixel area relation.ion, as it gives moire’-free results. But when the image is zoomed, 





 
import cv2
 
img = cv2.imread('lena.png')
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 220 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Original Dimensions :  (512, 512, 3) (height,width,layer)

#Resized Dimensions :  (1126, 1126, 3)  (height,width,layer)
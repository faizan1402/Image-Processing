import cv2

#imread(flag(o =means grayscale image and 1= color image))
img = cv2.imread ('faizan.jpg')
#print(img.shape)# value =(512= height ,512=width ,3=layer)
print("Original Dimensions:",img.shape)#means img of different differnt height and width pixl  


cv2.imshow('image',img)


cv2.waitKey(0)

cv2.destroyAllWindows()

#Output -Original Dimensions: (3840, 1958, 3)
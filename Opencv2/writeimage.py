import cv2


img = cv2.imread ('lena.png',-2)
#imread (read the image)
print(img.shape)
#show the pixl of image


cv2.imshow('original_imgage',img)
cv2.imwrite('copy_image.png',img)
cv2.imwrite('copy_image.jpg',img)


cv2.waitKey(0)
#wait key function basically when screen is stop 

cv2.destroyAllWindows()
# Means stop the all window

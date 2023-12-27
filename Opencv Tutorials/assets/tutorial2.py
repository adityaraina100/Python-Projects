import cv2
import random

img = cv2.imread('assets/image.jpg', -1)

# Change first 100 rows to random pixels
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

tag = img[500:700, 600:825]  
img[100:300, 600:825] = tag 

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

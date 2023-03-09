import cv2

img = cv2.imread('test.png')
print(img.shape)
img =cv2.resize(img, (500,500))
print(img.shape)
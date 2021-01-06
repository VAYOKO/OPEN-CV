import cv2

img = cv2.imread('colrshape1.jpg')

print(img.shape)
print(img.shape[0])
print(img.shape[1])
print(img.shape[2])

channels = cv2.split(img)
cv2.imshow('B',channels[1])
cv2.waitKey()
cv2.destroyAllWindows()

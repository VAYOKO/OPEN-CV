import cv2

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    R = frame[ :, :, 2]
    G = frame[ :, :, 1]
    B = frame[ :, :, 0]
    mask = (R < 10) & (G < 10) & (B > 50)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask*1.0)
    #cv2.imshow('R',R)
    #cv2.imshow('G',G)
    #cv2.imshow('B',B)
    cv2.waitKey(1)

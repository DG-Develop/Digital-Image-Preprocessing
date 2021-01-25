import cv2

img = cv2.imread("signature.png")

edge_img = cv2.Canny(img, 100, 200)

cv2.imshow('Signature', edge_img)

cv2.waitKey(0)
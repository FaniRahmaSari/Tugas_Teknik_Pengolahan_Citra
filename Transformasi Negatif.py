import cv2

img = cv2.imread("mammogram.jpg", 0)
img_1 = 255 - img

cv2.imshow("Original Pic", img)
cv2.imshow("Negative Pic", img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()
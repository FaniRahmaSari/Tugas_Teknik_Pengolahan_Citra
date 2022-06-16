import cv2
import numpy as np
img = cv2.imread("lena.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Default Pictures", img)
cv2.imshow("Grayscale Pictures", gray)

cv2.waitKey(0)
cv2.destoryAllWindows()
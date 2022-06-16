import cv2
import numpy as np

# load the source image
img = cv2.imread('lena.jpg')

# convert it to grayscale
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# apply histogram equalization
img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
hist_eq = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

# display both images (original and equalized)
cv2.imshow("equalizeHist", np.hstack((img, hist_eq)))
cv2.waitKey(0)
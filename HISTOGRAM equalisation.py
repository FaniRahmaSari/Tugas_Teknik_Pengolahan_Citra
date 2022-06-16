import numpy as np
import cv2 as cv
import matplotlib
import matplotlib.pyplot as plt
citra = cv.imread('lena.jpg')
histo = cv.calcHist([citra],[0],None,[256], [0, 256])
plt.plot(histo)
plt.show()

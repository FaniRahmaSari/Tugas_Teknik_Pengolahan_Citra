import cv2
import numpy as np
from  matplotlib import pyplot as plt

def Histogram(A):
    nilai_bin = 255
    A = A+1
    [frekuensi,value] = np.histogram(A,bins=nilai_bin)
    cumulatif_histogram = frekuensi.cumsum()
    [baris,kolom] = A.shape
    probabilty_frekuensi = np.round((cumulatif_histogram/float(A.size))*nilai_bin)
    B = np.empty(A.shape)
    for i in range(0,baris):
        for j in range(0,kolom):
            B[i,j] = probabilty_frekuensi[A[i,j]-1]
    return B

I = cv2.imread('lena.jpg')
gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY) #ubah ke format gray
hasil = Histogram(gray)
plt.figure('histogram')
plt.subplot(1,2,1),plt.imshow(gray,cmap='gray'),plt.title('gray')
plt.subplot(1,2,2),plt.imshow(hasil,cmap='gray'),plt.title('histogram')
plt.show()
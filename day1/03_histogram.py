import cv2
import numpy as np

I = cv2.imread("lena.png",0)

hist = np.zeros(256)

s = I.shape

for i in range(s[0]):
    for j in range(s[1]):
        pixel = I[i,j]
        hist[pixel] = hist[pixel]+1

import matplotlib.pyplot as plt
plt.plot(hist)

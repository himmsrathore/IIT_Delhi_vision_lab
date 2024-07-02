import cv2
import numpy as np
import matplotlib.pyplot as plt
I = cv2.imread("input.png",0)
s = I.shape


hist = np.zeros(256)
for i in range(s[0]):
    for j in range(s[1]):
        pixel = I[i,j]
        hist[pixel] = hist[pixel]+1
cum_hist = np.zeros(256)
cum_hist[0] = hist[0]
for i in range(1,256):
    cum_hist[i] = hist[i]+cum_hist[i-1]

plt.plot(cum_hist)
norm_cum_hist = cum_hist/cum_hist[-1]
norm_cum_hist = norm_cum_hist*255

new_image = np.zeros(s)

for i in range(s[0]):
    for j in range(s[1]):
        pixel = I[i,j]
        new_image[i,j] = round(norm_cum_hist[pixel])


cv2.imwrite("input_hist_eq.png",new_image)
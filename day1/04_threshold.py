import cv2

I = cv2.imread("lena.png",0)
s = I.shape

for i in range(s[0]):
    for j in range(s[1]):
        pixel = I[i,j]
        if pixel<=200:
            I[i,j] = 0
        else:
            I[i,j] = 255

cv2.imwrite("lena_threshold.png",I)
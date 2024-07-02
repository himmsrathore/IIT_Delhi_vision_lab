import cv2

I = cv2.imread("lena.png",0)
s = I.shape

for i in range(s[0]):
    for j in range(s[1]):
        pixel = I[i,j]
        I[i,j] = 255-pixel

cv2.imwrite("lena_negative.png",I)
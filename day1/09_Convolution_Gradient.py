import cv2
import numpy as np

I = cv2.imread("lena.png",0)
s = I.shape

#kernel = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
kernel = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
kernel = kernel/8
kernel_shape = kernel.shape
Ix = np.zeros((s[0]-kernel_shape[0]+1,s[1]-kernel_shape[1]+1))

for i in range(s[0]-kernel_shape[0]+1):
    for j in range(s[1]-kernel_shape[1]+1):
        part_image = I[i:i+kernel_shape[0],j:j+kernel_shape[1]]
        output = part_image*kernel
        Ix[i,j] = np.sum(output)
        
        
kernel = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
kernel = kernel/8
kernel_shape = kernel.shape
Iy = np.zeros((s[0]-kernel_shape[0]+1,s[1]-kernel_shape[1]+1))

for i in range(s[0]-kernel_shape[0]+1):
    for j in range(s[1]-kernel_shape[1]+1):
        part_image = I[i:i+kernel_shape[0],j:j+kernel_shape[1]]
        output = part_image*kernel
        Iy[i,j] = np.sum(output)


Ix = np.double(Ix)
Iy = np.double(Iy)
Ans = np.sqrt(Ix**2+Iy**2)

Ans_n = (Ans-np.min(Ans))/(np.max(Ans)-np.min(Ans))
Ans_n = Ans_n*255
Ans_n = np.uint8(Ans_n)        
cv2.imwrite("lena_gradient.png",Ans_n)
        
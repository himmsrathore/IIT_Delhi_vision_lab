import cv2
import numpy as np

I = cv2.imread("circle.png",0)
I = np.double(I)

def convolve(I,kernel):
    s =  I.shape
    kernel_shape = kernel.shape
    new_image = np.zeros((s[0]-kernel_shape[0]+1,s[1]-kernel_shape[1]+1))
    
    for i in range(s[0]-kernel_shape[0]+1):
        for j in range(s[1]-kernel_shape[1]+1):
            part_image = I[i:i+kernel_shape[0],j:j+kernel_shape[1]]
            output = part_image*kernel
            new_image[i,j] = np.sum(output)
    return new_image

Kx = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
Kx = Kx/8

Ky = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
Ky = Ky/8

Ix = convolve(I, Kx)
cv2.imwrite("temp_Ix.png",Ix)
Iy = convolve(I, Ky)


Ixx = convolve(Ix, Kx)
Ixy = convolve(Ix, Ky)
Iyy = convolve(Iy, Ky)

temp1 = Ixx*Iyy
temp2 = Ixy*Ixy
det = temp1-temp2
trace = Ixx+Iyy
trace_square = trace**2
temp3 = 0.06*trace_square
R = det-temp3
# R = det-0.06*trace_square

R_shape = R.shape
Corner_image = np.zeros(R_shape)
for i in range(R_shape[0]):
    for j in range(R_shape[1]):
        if R[i,j]>100:
            Corner_image[i,j]= 255
        else:
            Corner_image[i,j] = 0
            
cv2.imwrite("circle_color.png",Corner_image)
import matplotlib.pyplot as plt

plt.imshow(R)

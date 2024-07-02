import cv2
import numpy as np

I = np.zeros((512,512,3))
I[:,:,1] = 255
I[:,:,2] = 255

I = np.uint8(I)
cv2.imwrite("colour_image.png",I)
import cv2
import numpy as np

I = np.zeros((512,512))
I[0:256,0:256]  = 255
I[256:512,0:256] = 127
I[256:512,256:512] = 255

I = np.uint8(I)
cv2.imwrite("trial2.png",I)
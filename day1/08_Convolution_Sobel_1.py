#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:41:31 2024

@author: rohan
"""

import cv2
import numpy as np

I = cv2.imread("lena.png",0)
s = I.shape

kernel = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
kernel = kernel/9
kernel_shape = kernel.shape
Ix = np.zeros((s[0]-kernel_shape[0]+1,s[1]-kernel_shape[1]+1))

for i in range(s[0]-kernel_shape[0]+1):
    for j in range(s[1]-kernel_shape[1]+1):
        part_image = I[i:i+kernel_shape[0],j:j+kernel_shape[1]]
        output = part_image*kernel
        Ix[i,j] = np.sum(output)

cv2.imwrite("lena_edge_1.png",Ix)
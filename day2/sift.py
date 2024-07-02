#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:58:38 2024

@author: rohan
"""

import cv2
import numpy as np

def sift_feature_matching(img1_path, img2_path):
    # Load the images
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
    
    # Initialize the SIFT detector
    sift = cv2.SIFT_create()
    
    # Detect SIFT features and compute descriptors for both images
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    
    # Initialize the Brute Force matcher
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    
    # Match descriptors
    matches = bf.match(des1, des2)
    
    # Sort matches by distance (the lower the distance, the better the match)
    matches = sorted(matches, key=lambda x: x.distance)
    
    # Draw top matches
    #img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    # Calculate similarity score based on the number of good matches
    good_matches = [m for m in matches if m.distance < 10]
    similarity_score = len(good_matches) / len(matches)
    

    return similarity_score


img1_path = 'circle_color.png'
img2_path = 'lena.png'
similarity_score = sift_feature_matching(img1_path, img2_path)

print(f"Similarity score: {similarity_score}")

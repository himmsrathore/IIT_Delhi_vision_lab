import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the images
img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

# Check if images are loaded
if img1 is None:
    print("Error: Could not load image1.jpg")
    exit()
if img2 is None:
    print("Error: Could not load image2.jpg")
    exit()

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

# Print descriptors
print("Descriptors for image 1:\n", descriptors1)
print("Descriptors for image 2:\n", descriptors2)

# Initialize BFMatcher
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# Match descriptors
matches = bf.match(descriptors1, descriptors2)

# Sort matches by distance
matches = sorted(matches, key = lambda x:x.distance)

# Draw matches
img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Show the matched image
plt.imshow(img_matches)
plt.title('Feature Matching with SIFT')
plt.show()

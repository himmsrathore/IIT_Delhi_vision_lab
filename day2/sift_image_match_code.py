import cv2
import matplotlib.pyplot as plt

# Read images
image1 = cv2.imread("chetanc.png", 0)
image2 = cv2.imread("chetancc.png", 0)

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

# Create BFMatcher object
bf = cv2.BFMatcher()

# Match descriptors using KNN
matches = bf.knnMatch(descriptors1, descriptors2, k=2)

# Apply ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.3 * n.distance:
        good_matches.append(m)

# Draw matches
matched_image = cv2.drawMatches(image1, keypoints1, image2, keypoints2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the matched image
plt.figure(figsize=(10, 5))
plt.imshow(matched_image)
plt.title("Feature Matching using SIFT")
plt.show()

# Calculate and print the similarity score
similarity_score = len(good_matches) / len(keypoints1)
print(f"Similarity score: {similarity_score}")

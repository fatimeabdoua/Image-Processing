import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r'C:/Users/USER/PycharmProjects/Image Prosessing/Pictures/picture2.jpg', cv2.IMREAD_GRAYSCALE)

# Define the 3x3 and 5x5 averaging filters
filter_3x3 = np.ones((3, 3), np.float32) / 9
filter_5x5 = np.ones((5, 5), np.float32) / 25

# Apply the filters using OpenCV's filter2D function
smoothed_3x3 = cv2.filter2D(image, -1, filter_3x3)
smoothed_5x5 = cv2.filter2D(image, -1, filter_5x5)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(image, cmap="gray"), plt.title("Original Image")
plt.subplot(1, 3, 2), plt.imshow(smoothed_3x3, cmap="gray"), plt.title("3x3 Averaging Filter")
plt.subplot(1, 3, 3), plt.imshow(smoothed_5x5, cmap="gray"), plt.title("5x5 Averaging Filter")
plt.show()
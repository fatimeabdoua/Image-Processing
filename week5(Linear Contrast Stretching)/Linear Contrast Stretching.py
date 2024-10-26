import cv2
import numpy as np
import matplotlib.pyplot as plt


# Function for linear contrast stretching
def contrast_stretching(image):
    # Get minimum and maximum intensity values
    min_val = np.min(image)
    max_val = np.max(image)

    # Apply the contrast stretching formula
    stretched = ((image - min_val) / (max_val - min_val)) * 255
    return np.uint8(stretched)


# Load the image in grayscale
img = cv2.imread(r'C:/Users/USER/PycharmProjects/Image Prosessing/Pictures/picture1.jpg', 0)

# Check if the image is loaded correctly
if img is None:
    raise FileNotFoundError("Image file not found or path is incorrect")

# Apply linear contrast stretching
stretched_img = contrast_stretching(img)

# Plotting the original and contrast-stretched images along with their histograms
plt.figure(figsize=(12, 10))

# Original Image
plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')  # Hide axes

# Histogram of the Original Image
plt.subplot(2, 2, 2)
plt.title('Histogram of Original Image')
plt.hist(img.ravel(), bins=256, range=(0, 256), color='black', alpha=0.7)
plt.xlim([0, 256])

# Contrast-Stretched Image
plt.subplot(2, 2, 3)
plt.title('Contrast-Stretched Image')
plt.imshow(stretched_img, cmap='gray')
plt.axis('off')  # Hide axes

# Histogram of the Contrast-Stretched Image
plt.subplot(2, 2, 4)
plt.title('Histogram of Contrast-Stretched Image')
plt.hist(stretched_img.ravel(), bins=256, range=(0, 256), color='black', alpha=0.7)
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
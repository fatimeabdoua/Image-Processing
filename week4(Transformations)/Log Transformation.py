import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread(r'C:/Users/USER/PycharmProjects/Image Prosessing/Pictures/picture1.jpg', 0)  # Grayscale image

# Check if the image is loaded
if img is None:
    raise FileNotFoundError("Image file not found or path is incorrect")

# Convert the image to float32 to prevent overflow and ensure precision
img = img.astype(np.float32)

# Prevent divide by zero and overflow issues
epsilon = 1e-5  # Small constant to prevent log(0) and overflow
img = img + epsilon  # Add epsilon to all pixel values

# Apply log transformation
c = 1
#c = 255 / np.log(1 + np.max(img))  # Calculate scaling constant based on maximum pixel value
log_transformed = c * np.log(1 + img)  # Apply log transformation

# Clip values to the valid range [0, 255] for image data
log_transformed = np.clip(log_transformed, 0, 255)

# Convert the transformed image back to uint8 format (0-255)
log_transformed = log_transformed.astype(np.uint8)

# Display original and log transformed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Log Transformed Image')
plt.imshow(log_transformed, cmap='gray')

plt.show()
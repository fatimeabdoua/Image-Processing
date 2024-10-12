import cv2
import numpy as np
import matplotlib.pyplot as plt


# Function to perform gamma correction
def gamma_correction(image, gamma):
    # Normalize the image to range [0, 1]
    normalized_image = image / 255.0

    # Apply gamma correction
    corrected_image = np.power(normalized_image, gamma)

    # Scale back to [0, 255] and convert to uint8
    corrected_image = np.uint8(corrected_image * 255)

    return corrected_image


# Load the image in grayscale
img = cv2.imread(r'C:/Users/USER/PycharmProjects/Image Prosessing/Pictures/picture1.jpg', 0)

# Check if the image is loaded correctly
if img is None:
    raise FileNotFoundError("Image file not found or path is incorrect")

# Apply gamma correction with different gamma values
gamma_low = gamma_correction(img, 0.5)  # Gamma < 1 for brighter output
gamma_high = gamma_correction(img, 2.0)  # Gamma > 1 for darker output

# Display original and gamma-corrected images
plt.figure(figsize=(15, 5))

# Original image
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')

# Gamma < 1 (brightened)
plt.subplot(1, 3, 2)
plt.title('Gamma 0.5 (Brightened)')
plt.imshow(gamma_low, cmap='gray')

# Gamma > 1 (darkened)
plt.subplot(1, 3, 3)
plt.title('Gamma 2.0 (Darkened)')
plt.imshow(gamma_high, cmap='gray')

plt.show()
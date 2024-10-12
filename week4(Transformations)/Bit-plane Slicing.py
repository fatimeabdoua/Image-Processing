import cv2
import numpy as np
import matplotlib.pyplot as plt


# Function to extract a specific bit-plane from an image
def bit_plane_slicing(image, bit):
    # Right shift the image and extract the specific bit
    return np.bitwise_and(image, 1 << bit) >> bit


# Function to reconstruct the image from selected bit planes
def reconstruct_image(bit_planes):
    # Initialize the reconstructed image with zeros
    reconstructed_image = np.zeros_like(bit_planes[0])

    # Sum the selected bit planes to reconstruct the image
    for plane in bit_planes:
        reconstructed_image += plane

    return reconstructed_image


# Load the image in grayscale
img = cv2.imread(r'C:/Users/USER/PycharmProjects/Image Prosessing/Pictures/picture1.jpg', 0)

# Check if the image is loaded correctly
if img is None:
    raise FileNotFoundError("Image file not found or path is incorrect")

# Create an empty list to store the bit planes
bit_planes = []

# Extract each bit plane (from 0 to 7)
for i in range(8):
    bit_plane = bit_plane_slicing(img, i)
    bit_planes.append(bit_plane)

# Reconstruct the image from all bit planes
reconstructed_image = reconstruct_image(bit_planes)

# Plot the original image, bit planes, and reconstructed image
plt.figure(figsize=(15, 12))

# Original Image
plt.subplot(4, 3, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')  # Hide axes

# Display each bit plane
for i in range(8):
    plt.subplot(4, 3, i + 2)
    plt.title(f'Bit-plane {i}')
    plt.imshow(bit_planes[i] * 255, cmap='gray')  # Scale for display
    plt.axis('off')  # Hide axes

# Reconstructed Image
plt.subplot(4, 3, 10)
plt.title('Reconstructed Image')
plt.imshow(reconstructed_image, cmap='gray')
plt.axis('off')  # Hide axes

plt.tight_layout()
plt.show()
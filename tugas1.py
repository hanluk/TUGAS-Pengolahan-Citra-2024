modified_code = '''#pip install numpy
import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# Load the image
image = img.imread("D:/source.jpg")

# Extract individual color channels
red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

# Create images for each channel by zeroing out the other channels
imgRed = np.zeros_like(image)
imgRed[:, :, 0] = red

imgGreen = np.zeros_like(image)
imgGreen[:, :, 1] = green

imgBlue = np.zeros_like(image)
imgBlue[:, :, 2] = blue

# Display the original image and the individual channels
plt.figure(figsize=(10, 15))
plt.subplot(4, 1, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(4, 1, 2)
plt.title("Red Channel")
plt.imshow(imgRed)

plt.subplot(4, 1, 3)
plt.title("Green Channel")
plt.imshow(imgGreen)

plt.subplot(4, 1, 4)
plt.title("Blue Channel")
plt.imshow(imgBlue)

plt.show()
'''


with open(file_path, 'w') as file:
    file.write(modified_code)

modified_code

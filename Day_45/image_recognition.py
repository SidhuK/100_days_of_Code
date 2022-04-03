# A python script that finds the most common colours in an uploaded image.

# Importing Modules
# Colorthief based on Pillow, makes finding colors easier
from colorthief import ColorThief

# Numpy to build an array from the palette
import numpy as np

# Matplotlib to show the image
import matplotlib.pyplot as plt

# Upload image using colorthief
image = ColorThief("image.jpg")

# Get the top 7 Colors
top7colors = ColorThief.get_palette(image, color_count=7)
print(top7colors)


# Convert top 7 colors into a numpy array
palette = np.array(top7colors)[np.newaxis, :, :]


# plot those colors using matplotlib
plt.imshow(palette)
plt.axis('off')
plt.show()


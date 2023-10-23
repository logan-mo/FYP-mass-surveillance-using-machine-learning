import cv2
from matplotlib import pyplot as plt
import numpy as np

# Read the input image
img = cv2.imread("red_CAr.jpg")


# define a function to compute and plot histogram
def plot_histogram(img, title, mask=None):
    # split the image into blue, green and red channels
    channels = cv2.split(img)
    colors = ("b", "g", "r")
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    # loop over the image channels
    for channel, color in zip(channels, colors):
        # compute the histogram for the current channel and plot it
        hist = cv2.calcHist([channel], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])


# define a mask for our image; black for regions to ignore

# and white for regions to examine
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (160, 130), (410, 290), 255, -1)

# display the masked region
masked = cv2.bitwise_and(img, img, mask=mask)

# compute a histogram for masked image
plot_histogram(img, "Histogram for Masked Image", mask=mask)

# show the plots
plt.show()
cv2.imshow("Mask", mask)
cv2.imshow("Mask Image", masked)
cv2.waitKey(0)

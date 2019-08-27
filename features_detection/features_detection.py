# featres_detection.py

import cv2
import numpy as np
from matplotlib import pyplot as plt
import opencv.zhang_suen as thinning

img = cv2.imread("./opencv/fingerprint.png", 0)
h, w = img.shape
img = cv2.resize(img, (int(h * 0.5), int(w * 0.5)))
img = cv2.medianBlur(img, 5)
img = cv2.GaussianBlur(img, (5, 5), 0)

# ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
# th = cv2.adaptiveThreshold(
#     img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
# )

th = cv2.bitwise_not(th)

plt.imshow(th)
plt.title("thresholded")
plt.show()

# th = cv2.bitwise_not(th)

kernel = np.ones((3, 3), np.uint8)
# erosion = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
erosion = cv2.erode(erosion, kernel, iterations=1)

plt.imshow(erosion)
plt.title("erosion")
plt.show()

thined = thinning.ZhangSuen(erosion)
# thined = cv2.ximgproc.thinning(th)

plt.imshow(thined, cmap="gray")
plt.title("thined")
plt.show()

# thined
# rows, columns = thined.shape
# feature_points = np.zeros((rows, columns))
# for x in range(1, rows - 1):
#     for y in range(1, columns - 1):
#         if thined[x][y] == 1:
#             neighbour_points = thined[x-1][y-1] + thined[x][y-1] + thined[x+1][y-1] +thined[x-1][y] + thined[x+1][y] + thined[x-1][y+1] + thined[x][y+1] + thined[x+1][y+1]
#             if (neighbour_points == 1 || neighbour_points == 3):
#                 feature_points[x][y] = neighbour_points


# gray1 = cv2.cvtColor(thined, cv2.COLOR_BGR2GRAY)
akaze = cv2.AKAZE_create()
kp1 = akaze.detect(thined)
fetures = cv2.drawKeypoints(thined, kp1, None, flags=4)

plt.imshow(fetures)
plt.title("fetures")
plt.show()

plt.imshow(fetures)
plt.title("fetures")
plt.savefig("result.png")

# featres_detection.py

import cv2
import numpy as np
from matplotlib import pyplot as plt
# import features_detection.zhang_suen as thinning

img = cv2.imread("./fingerprint.png", 0)
h, w = img.shape
img = cv2.resize(img, (int(h * 1), int(w * 1)))
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
erosion = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
erosion = cv2.erode(erosion, kernel, iterations=1)

plt.imshow(erosion)
plt.title("erosion")
plt.show()

# thined = thinning.ZhangSuen(erosion)

height, width = img.shape
thined = np.zeros((height, width), np.uint8)
thined = cv2.ximgproc.thinning(th,thined,cv2.ximgproc.THINNING_GUOHALL)

plt.imshow(thined, cmap="gray")
plt.title("thined")
plt.show()

# gray1 = cv2.cvtColor(thined, cv2.COLOR_BGR2GRAY)
# akaze = cv2.AKAZE_create()
# kp1 = akaze.detect(thined)
# fetures = cv2.drawKeypoints(thined, kp1, None, flags=4)

# plt.imshow(fetures)
# plt.title("fetures")
# plt.show()

# plt.imshow(fetures)
# plt.title("fetures")
# plt.savefig("result.png", dpi=3000)


thined = thined.astype(np.uint32)
height, width = thined.shape
for y in range(0, height - 1):
    for x in range(0, width - 1):
        if y == 0 or y == height - 1 or x == 0 or x == width - 1:
            thined[y][x] = 0

neighbour_point_map = np.zeros((height, width), np.uint32)
for y in range(1, height - 2):
    for x in range(1, width - 2):
        if thined[y][x] == 255:
            neighbour_point = thined[y-1][x-1] + thined[y][x-1] + thined[y+1][x-1] +thined[y-1][x] + thined[y+1][x] + thined[y-1][x+1] + thined[y][x+1] + thined[y+1][x+1]
            neighbour_point_map[y][x] = neighbour_point

yellows = 0
reds = 0

plt.imshow(thined, cmap="gray")
for y in range(1, height - 2):
    for x in range(1, width - 2):
        if neighbour_point_map[y][x] == 255:
            plt.scatter(x, y, marker='.', linewidths=0.3, facecolor='None', edgecolors='yellow', alpha='0.5')
            yellows += 1
        if neighbour_point_map[y][x] == 765:
            # if not ( neighbour_point_map[y-2][x-2] >= 765 or neighbour_point_map[y-2][x-1] >= 765 or neighbour_point_map[y-2][x] >= 765 or neighbour_point_map[y-1][x-2] >= 765 or neighbour_point_map[y-1][x-1] >= 765 or neighbour_point_map[y-1][x] >= 765 or neighbour_point_map[y][x-2] >= 765 or neighbour_point_map[y][x-1] >= 765 ):
            if not ( neighbour_point_map[y-1][x-1] >= 765 or neighbour_point_map[y][x-1] >= 765 or neighbour_point_map[y+1][x-1] >= 765 or neighbour_point_map[y+1][x] >= 765 ):
                plt.scatter(x, y, marker='.', linewidths=0.3,  facecolor='None', edgecolors='red', alpha='0.5')
                reds += 1
plt.title("fetures")
plt.savefig("result.png", dpi=1000)
print("２分岐: " + str(yellows))
print("３分岐: " + str(reds))

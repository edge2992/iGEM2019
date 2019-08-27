# threshold.py
# http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./02_opencv/fingerprint.png", 0)
img = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

titles = [
    "Original Image",
    "Global Thresholding (v = 127)",
    "Adaptive Mean Thresholding",
    "Adaptive Gaussian Thresholding",
]
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

img = cv2.imread("./02_opencv/fingerprint.png", 0)
blur = cv2.bilateralFilter(img, 9, 75, 75)

ret, blur_th1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
blur_th2 = cv2.adaptiveThreshold(
    blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
blur_th3 = cv2.adaptiveThreshold(
    blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

titles = [
    "blur Image",
    "blur Global Thresholding (v = 127)",
    "blur Adaptive Mean Thresholding",
    "blur Adaptive Gaussian Thresholding",
]
images = [blur, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

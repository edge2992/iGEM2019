import cv2
import numpy as np

img1 = cv2.imread('moji1.jpeg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow("test", gray1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# exit(0)
sift = cv2.xfeatures2d.SIFT_create()
kp1 = sift.detect(gray1)
img1_sift = cv2.drawKeypoints(gray1, kp1, None, flags=4)
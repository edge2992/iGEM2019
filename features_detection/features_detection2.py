# featres_detection2.py

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os



def thinner(filename):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print('failed to load image.')
        print(filename)
        return 0

    height, width = img.shape
    # print("{}, {}".format(height, width))
    img = cv2.medianBlur(img, 5)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # 画像の閾値処理
    th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    th = cv2.bitwise_not(th)  # bit反転

    # モルフォロジー変換　クロージング
    # 膨張の後に収縮することで、小さな穴を埋めるのに役立つ
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
    # 収縮
    erosion = cv2.erode(erosion, kernel, iterations=1)

    thined = cv2


    plt.imshow(erosion)
    plt.title("erosion")
    plt.show()

    return erosion


def main():
    thinner("./fingerprint.png")


if __name__ == "__main__":
    main()
    exit()


# http://モザイクqiita.com/yuukami1024/items/c1d7eea01a46de91829f

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def trim(img):
    height = img.shape[0]
    width = img.shape[1]
    image6 = img[100:height-40, 100:width-40]
    return image6


def zero_one(image):
    output_width = 800
    # font_aspext = 1.8
    font_aspext = 1.0
    ikichi = 180

    im_gray = cv2.imread(image, 0)
    im_gray = trim(im_gray)

    # 倍率を指定
    # im_gray = cv2.resize(im_gray, 0.5, 0.5)
    if im_gray is None:
        # 読み込みに失敗した場合は None が返る。
        print('failed to load image.')

    height = im_gray.shape[0]
    width = im_gray.shape[1]

    if width > output_width:
        im_resized = cv2.resize(im_gray, (output_width, int((output_width / width) * height / font_aspext)))
    else:
        im_resized = cv2.resize(im_gray, (width, int(height / font_aspext)))

    ret, th = cv2.threshold(im_resized, ikichi, 255, cv2.THRESH_BINARY)

    th[th != 0] = 1
    # 画像を表示
    plt.imshow(th)
    plt.show()
    # print(type(th))
    np.savetxt("../data/save.txt", th, "%d")
    print("Complete")


def main():
    print("start")
    image = "img/fingerprint.png"
    zero_one(image)


if __name__ == '__main__':
    main()

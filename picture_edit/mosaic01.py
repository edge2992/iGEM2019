# http://モザイクqiita.com/yuukami1024/items/c1d7eea01a46de91829f

import cv2
import numpy as np
import matplotlib.pyplot as plt


def zero_one(image):
    output_width = 300
    # font_aspext = 1.8
    font_aspext = 1.0
    ikichi = 180

    im_gray = cv2.imread(image, 0)
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

    # print(th)
    # print(type(th))

    # 画像を表示
    plt.imshow(th)
    plt.show()

    # write.txtに出力
    f = open("img/write.txt", "w")
    for array in th:  # 各行について
        row = map(str, array)
        line = "".join(row)
        line.replace("[", "")
        line.replace("]", "")
        line.replace(" ", "")  # 強引ですみませんm(_ _)m
        f.write(line)
        f.write("\n")
    f.close()  # 閉じる
    print("Complete")


def main():
    print("start")
    image = "img/fingerprint.png"
    zero_one(image)


if __name__ == '__main__':
    main()

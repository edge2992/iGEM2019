import cv2
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
# 参考　http://モザイクqiita.com/yuukami1024/items/c1d7eea01a46de91829f


class Mosaic:
    # Todo: 正方形のみに対応中　picture th
    output_width = 400
    threshold = 180

    def __init__(self, width=output_width, threshold_num=threshold):
        self.output_width = width
        self.threshold = threshold_num
        self.th = np.zeros((self.output_width, self.output_width))
        # self.mosaic(filename)

    def set_th(self, th):
        self.th = th

    def mosaic(self, filename):
        """
        モザイク処理する
        :param filename:　fileの場所
        :return:
        """
        im_gray = cv2.imread(filename, 0)

        if im_gray is None:
            print('failed to load image.')
            print(filename)
            return 0

        height = im_gray.shape[0]
        width = im_gray.shape[1]

        im_resize = cv2.resize(im_gray, (self.output_width, int((self.output_width / width) * height)))
        ret, th = cv2.threshold(im_resize, self.threshold, 255, cv2.THRESH_BINARY)

        th[th != 0] = 1
        self.th = th
        return self.th

    def trim(self, left=0., right=1., top=0., bottom=1.):
        """
        トリミングする
        :param left: 0~1
        :param right: 0~1
        :param top: 0~1
        :param bottom: 0~1
        :return:
        """
        height = self.th.shape[0]
        width = self.th.shape[1]

        if (left > right) or (top > bottom):
            print("left & top should be lower than right & bottom")
        elif (0 > left) and (left > 1):
            print("parameter left should be 0 to 1")
        elif (0 > right) and (right > 1):
            print("parameter right should be 0 to 1")
        elif (0 > top) and (top > 1):
            print("parameter top should be 0 to 1")
        elif (0 > bottom) and (bottom > 1):
            print("parameter bottom should be 0 to 1")
        else:
            img_trim = self.th[int(height * top):int(height * bottom), int(width * left):int(width * right)]
            self.th = img_trim
        return self.th

    def make_blank(self, size=50, num=5):
        """
        画像を欠損させる
        :param size: 正方形のサイズ
        :param num: 正方形の数
        :return: ndarray
        """
        for i in range(num):
            a = nr.randint(0, self.th.shape[0] - size - 1)
            b = nr.randint(0, self.th.shape[0] - size - 1)
            # print(a)
            self.th[a:a + size, b:b + size] = np.zeros((size, size))
        return self.th

    def save(self, filename):
        np.savetxt(filename, self.th, "%d")

    def show(self):
        plt.figure()
        plt.imshow(self.th)
        plt.show()


# thのサイズが合わない気がする
def main():
    image = "img/fingerprint.png"
    save_img = "../data/save_big.txt"
    Mos = Mosaic()
    Mos.mosaic(image)
    # Mos.trim(left=0.2, right=0.5, top=0.2, bottom=0.5)
    # Mos.make_blank()
    Mos.show()
    Mos.save(save_img)


if __name__ == '__main__':
    main()
    exit()

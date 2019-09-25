from Young.Young_pattern import Young_Pattern
import numpy as np
import matplotlib.pyplot as plt


class Ndarray_Structure:
    width = 100
    height = 100

    def __init__(self):
        """
        コンストラクタ（適当）
        """
        self.th = np.zeros((100, 100))

    def set_th(self, th):
        """
        状態を外から持ってくる
        :param th: ndarray
        """
        self.th = th
        self.height = th.shape[0]
        self.width = th.shape[1]

    def save(self, filename):
        """
        ファイルに書き込みする
        :param filename:
        """
        np.savetxt(filename, self.th, "%d")

    def show(self):
        """
        pyplotで確認する
        """
        plt.imshow(self.th)
        plt.show()



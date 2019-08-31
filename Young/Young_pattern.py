import numpy as np
from scipy import signal
import cv2
from Young.dots import Make_mask
import matplotlib.pyplot as plt


class Young_Pattern:
    width = 300  # 格子の横幅
    height = 300  # 格子の縦幅
    generation = 0

    def __init__(self, r1, r2, w1, w2, init_alive_prob=0.5):
        """
        コンストラクタ
        :param r1: radius of inner circle
        :param r2: radius of outer circle
        :param w1: parameter of inner circle
        :param w2: parameter of outer circle
        :param init_alive_prob: percentage of the number of initial black
        """
        self.mask = Make_mask(r1, r2, w1, w2)
        self.r1 = r1
        self.r2 = r2
        self.w1 = w1
        self.w2 = w2
        self.generation = 0
        self.state = self.init_state(self.width, self.height, init_alive_prob)

    def init_state(self, width=width, height=height, init_alive_prob=0.5):
        """
        初期化
        :param height: 格子の横幅
        :param width: 格子の縦幅
        :param init_alive_prob: percentage of the number of initial black
        :return: ndarray  state
        """
        self.width = width
        self.height = height
        N = self.width * self.height
        v = np.array(np.random.rand(N) + init_alive_prob, dtype=int)
        self.state = v.reshape(self.height, self.width)
        self.generation = 0
        return self.state

    def next_generation(self):
        """
        次の世代にstateを更新する
        :return: ndarray  state
        """
        N = signal.correlate2d(self.state, self.mask, mode="same", boundary="wrap")
        self.state = N > 0
        self.generation += 1
        return self.state

    def to_image(self, w=800, h=800):
        """
        imageをcv2で出力する
        :param w: resize to display by cv2
        :param h: resize to display by cv2
        :return: cv2
        """
        img = np.array(self.state, dtype=np.uint8) * 255
        img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)
        return img

    def load_text(self, filename):
        """
        初期値としてndarrayを他のファイルから取ってくる
        :param filename:
        """
        if cv2.os.path.exists(filename):
            self.state = np.loadtxt(filename)
            self.width = self.state.shape[0]
            self.height = self.state.shape[1]
            self.generation = 0
        else:
            print("file is not existed")
        return self.state

    def save_text(self, filename):
        """
        ndarrayをファイルに保存する
        :param filename:
        """
        np.savetxt(filename, self.state, "%d")

    def far_generation(self, generation):
        """
        generation世代後にstateを変更する
        :param generation: 世代数
        :return:
        """
        for i in range(generation):
            self.next_generation()
        return self.state

    def save_img(self, filename):
        """
        matplotlib 出力と保存
        """
        plt.figure()
        plt.imshow(self.state, cmap='pink', vmin=0, vmax=1)
        plt.savefig(filename + ".png")
        plt.show()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


def main():
    YP = Young_Pattern(3, 6, 1.0, -0.3, 0.08)


if __name__ == "__main__":
    main()
    exit()

import cv2
from scipy import signal
import numpy as np
from Young.Young_check import Young_Check
import matplotlib.pyplot as plt


class Young_Finger(Young_Check):
    __r_fn = 0.5
    __r_rd = 5

    def __init__(self, filename, r1, r2, w1, w2, init_alive_prob=0.5):
        self.__filename = filename
        super(Young_Check, self).__init__(r1, r2, w1, w2, init_alive_prob)
        self.img_finger = self.load_text(filename)
        self.__noise = np.zeros((self.width, self.height))
        self.noise()
        # print(self.__noise)

    def init_state(self, width=120, height=120, init_alive_prob=0.5):
        """
        初期化
        :param height: 格子の横幅
        :param width: 格子の縦幅
        :param init_alive_prob: percentage of the number of initial black
        :return: ndarray  state
        """
        self.state = self.load_text(self.__filename)
        return self.state

    def noise(self):
        N = self.width * self.height
        v = np.array(np.random.rand(N), dtype=float)
        self.__noise = v.reshape(self.height, self.width)
        return self.__noise

    def set_r_fn(self, r):
        self.__r_fn = r

    def set_r_rd(self, r):
        self.__r_rd = r

    def next_generation(self):
        """
        次の世代にstateを更新する
        :return: ndarray  state
        """
        N = signal.correlate2d(self.state, self.mask, mode="same", boundary="wrap")
        N = N * (1 - self.__r_fn) + self.img_finger * self.__r_fn + self.noise() * self.__r_rd
        self.state = N > 0
        return self.state

    def show_ini_end(self, filename, gen=30):
        fig, ax = plt.subplots(ncols=2,
                               sharex="col", sharey="all",
                               facecolor="lightgray")
        fig.suptitle('r1={0:.2g} r2={1:.2g} w1={2:.2g} w2={3:.2g} r_fn={4:.2g} r_rd={5:.2g} gen={6:.2g}'.format(self.r1, self.r2, self.w1, self.w2, self.__r_fn, self.__r_rd, gen), fontsize=9)
        ax[0].imshow(self.init_state(), cmap='pink')
        ax[0].set_title("initial state ", fontsize=7)
        ax[1].imshow(self.far_generation(gen), cmap='pink')
        ax[1].set_title("generation={0:.2g} ".format(gen), fontsize=7)
        plt.savefig("../data/compare_finger_" + filename + ".png")
        plt.show()


BackendError = type('BackendError', (Exception,), {})


def change(r_fn, r_rd):
    gen = 30
    r1 = 3
    r2 = 6
    w1 = 16.0
    w2 = -5.0
    fig, ax = plt.subplots(ncols=r_rd.size, nrows=r_fn.size,
                           sharex="col", sharey="all",
                           facecolor="lightgray")
    fig.suptitle('r1={0:.2g} r2={1:.2g} w1={2:.2g} w2={3:.2g} gen={4:.2g}'.format(r1, r2, w1, w2, gen), fontsize=9)
    for aline, r1 in zip(ax, r_fn):
        for elem, r2 in zip(aline, r_rd):
            YP = Young_Finger(3, 6, 16.0, -5.0, 0.08)
            YP.set_r_fn(r1)
            YP.set_r_rd(r2)
            elem.imshow(YP.far_generation(gen), cmap='pink')
            elem.set_title("r_fn={0:.2g} r_rd={1:.2g}".format(r1, r2), fontsize=7)
    plt.savefig("finger_rfn_rrd.png")
    plt.show()


def main():
    filename = "../data/save_big.txt"
    YP = Young_Finger(filename, 3, 6, 16.0, -5.0, 0.08)
    YP.show_ini_end("big")
    # gen = 30
    # r1 = 3
    # r2 = 6
    # w1 = 16.0
    # w2 = -5.0
    # YF = Young_Finger(r1, r2, w1, w2, 0.08)
    # #
    # # YF = Young_Finger(3, 6, 1.0, -0.3, 0.08)
    # YF.set_r_fn(0.1)
    # YF.set_r_rd(30)
    # YF.far_generation(30)
    # YF.show()
    # # YF.check_plot()
    # YF.show_cv2()
    #
    # r = np.array([20.0, 5.0, 1.0])
    # r2 = np.array([0.5, 0.2, 0.1])
    # change(r2, r)



if __name__ == "__main__":
    main()
    exit()




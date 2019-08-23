import cv2
from scipy import signal
import numpy as np
from Young.Young_check import Young_Check
import matplotlib.pyplot as plt


class Young_Finger(Young_Check):
    __r_fn = 0.001
    __r_rd = 0.1

    def __init__(self, r1, r2, w1, w2, init_alive_prob=0.5):
        super(Young_Check, self).__init__(r1, r2, w1, w2, init_alive_prob)
        self.img_finger = self.load_text("../data/save.txt")
        self.__noise = np.zeros((self.width, self.height))
        self.noise()

    def noise(self):
        N = self.width * self.height
        v = np.array(np.random.rand(N), dtype=int)
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


BackendError = type('BackendError', (Exception,), {})


def change(r_fn, r_rd):
    gen = 100
    fig, ax = plt.subplots(ncols=r_fn.size, nrows=r_rd.size,
                           sharex="col", sharey="all",
                           facecolor="lightgray")
    fig.suptitle('r1={0:.2g} r2={1:.2g} w1={2:.2g} w2={3:.2g} gen={4:.2g}'.format(3, 6, 1.0, -0.3, gen), fontsize=9)
    for aline, r1 in zip(ax, r_fn):
        for elem, r2 in zip(aline, r_rd):
            YP = Young_Finger(3, 6, 1.0, -0.3, 0.08)
            YP.set_r_fn(r1)
            YP.set_r_rd(r2)
            elem.imshow(YP.far_generation(gen), cmap='pink')
            elem.set_title("r_fn={0:.2g} r_rd={1:.2g}".format(r1, r2), fontsize=7)
    plt.savefig("result.png")
    plt.show()


def is_visible(winname):
    # cv2の閉じるエラーを解決したい（未解決）
    try:
        ret = cv2.getWindowProperty(
            winname, cv2.WND_PROP_VISIBLE
        )

        if ret == -1:
            raise BackendError('Use Qt as backend to check whether window is visible or not.')

        return bool(ret)

    except cv2.error:
        return False


def show_cv2():
    winname = "finger_print"
    YP = Young_Finger(3, 6, 1.0, -0.3, 0.08)
    # ret = 0
    wait = 50

    while True:
        img = YP.to_image()
        cv2.imshow(winname, img)
        ret = cv2.waitKey(wait)
        YP.next_generation()
        # prop_val = cv2.getWindowProperty(winname, cv2.WND_PROP_ASPECT_RATIO)
        if ret == ord('r'):
            YP.init_state(init_alive_prob=0.08)
        if ret == ord('s'):
            wait = min(wait * 2, 1000)
        if ret == ord('f'):
            wait = max(wait // 2, 10)
        if ret == ord('q') or ret == 27:
            break
        if not is_visible(winname):
            break
        if ret == ord('w'):
            YP.save_text("../data/save.txt")
        if ret == ord('l'):
            YP.load_text("../data/save.txt")
    cv2.waitKey(1)  # macの都合
    # cv2.destroyWindow('finger print')
    cv2.destroyAllWindows()
    # cv2.waitKey()  # macの都合
    return 0


def main():
    r = np.array([0.3, 0.1, 0.01, 0.001])
    change(r, r)


if __name__ == "__main__":
    main()
    exit()




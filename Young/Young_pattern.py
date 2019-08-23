import numpy as np
from scipy import signal
import cv2
from Young.dots import Make_mask
import matplotlib.pyplot as plt


class Young_Pattern:
    width = 300  # 格子の横幅
    height = 300  # 格子の縦幅

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
        self.__r1 = r1
        self.__r2 = r2
        self.__w1 = w1
        self.__w2 = w2
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
        return self.state

    def next_generation(self):
        """
        次の世代にstateを更新する
        :return: ndarray  state
        """
        N = signal.correlate2d(self.state, self.mask, mode="same", boundary="wrap")
        self.state = N > 0
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

    def show(self):
        """
        matplotlib 出力
        """
        plt.figure()
        plt.imshow(self.state, cmap='pink', vmin=0, vmax=1)
        plt.show()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


BackendError = type('BackendError', (Exception,), {})


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


def main():
    winname = "finger_print"
    YP = Young_Pattern(3, 6, 1.0, -0.3, 0.08)
    # ret = 0
    wait = 50

    while True:
        img = YP.to_image()
        cv2.imshow(winname, img)
        ret = cv2.waitKey(wait)
        YP.next_generation()
        prop_val = cv2.getWindowProperty(winname, cv2.WND_PROP_ASPECT_RATIO)
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


if __name__ == "__main__":
    main()
    exit()

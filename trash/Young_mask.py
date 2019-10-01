from trash.Young_check import Young_Check
from scipy import signal
import numpy as np

from picture_edit.mosaic_pic import Mosaic


class Young_Mask(Young_Check):

    def __init__(self, r1, r2, w1, w2, mask=np.ones((1, 1)), init_alive_prob=0.5):
        super(Young_Mask, self).__init__(r1, r2, w1, w2, init_alive_prob)
        self.out_mask = mask

    def set_mask(self, mask):
        self.out_mask = mask

    def square_mask(self):
        print(self.get_height())
        print(self.get_width())
        A = np.ones((self.get_width(), self.get_height()))
        Mos = Mosaic()
        Mos.set_th(A)
        B = Mos.make_blank(50, 10)
        C = (B == 0) * 2.0
        C += B
        Mos.show()
        Mos.set_th(C)
        Mos.show()
        print(C)
        self.out_mask = C

    def next_generation(self):
        """
        次の世代にstateを更新する
        :return: ndarray  state
        """
        N = signal.correlate2d(self.state, self.mask, mode="same", boundary="wrap")
        N *= self.out_mask
        self.state = N > 0
        # print("super")
        return self.state


def main():
    # ここには書かないようにする
    YM = Young_Mask(6, 16, 1.0, -0.3)
    YM.square_mask()
    YM.show_cv2()
    # YM.far_generation(50)
    # YM.show()


if __name__ == "__main__":
    main()
    exit()


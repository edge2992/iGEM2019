from Young.Young_pattern import Young_Pattern
import numpy as np
import matplotlib.pyplot as plt

from nakano.image_processing import thinning
from nakano.width_getter import get_width
from sawa.numpy_lin import Ndarray_Structure

# 横縞でサイズを図ろうとしたけどいらない
class Zebra(Ndarray_Structure):
    def make_zebra(self, width=1):
        zeros = np.ones((1, 200))
        ones = np.zeros((1, 200))
        arr = np.empty((0, 200), int)

        for i in range(int(100/width)):
            for j in range(width):
                arr = np.append(arr, zeros, axis=0)
            for l in range(width):
                arr = np.append(arr, ones, axis=0)

        self.th = arr


def main():
    for a1 in range(2, 6):
        YP = Young_Pattern(a1, a1 * 2, 16, -5)
        YP.far_generation(10)
        # YP.show()
        img = Ndarray_Structure()
        img.set_th(YP.state)
        img.multiple(255)
        print(type(img.th))
        thined = thinning(img.th, debug=True)
        print(type(thined))
        width = get_width(thined, debug=True)
        print("r1:　" + str(a1) + "　最頻値(幅): " + str(width))


if __name__ == "__main__":
    main()
    exit()


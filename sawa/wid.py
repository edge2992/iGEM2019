from Young.Young_pattern import Young_Pattern
import numpy as np
import matplotlib.pyplot as plt
from sawa.numpy_lin import Ndarray_Structure


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
    zebra = Zebra()
    zebra.make_zebra(50)
    zebra.show()
    YP = Young_Pattern(3, 6, 16, -5)
    YP.load_ndarray(zebra.th)
    YP.far_generation(20)
    print(YP.state)
    YP.save_img("data/1")


if __name__ == "__main__":
    main()
    exit()


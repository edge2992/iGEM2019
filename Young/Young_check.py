from Young.Young_pattern import Young_Pattern
import matplotlib.pyplot as plt
import numpy as np


class Young_Check(Young_Pattern):
    def __init__(self, r1, r2, w1, w2, init_alive_prob=0.5):
        super(Young_Check, self).__init__(r1, r2, w1, w2, init_alive_prob)

    def sum(self, generation=2):
        C = self.far_generation(generation)
        return C.sum()

    def check(self, width=100, height=100, generation=30):
        self.init_state(width, height)
        num = self.sum(generation)
        return num < width*height*0.9 or num > width*height*0.1

    def check_plot(self):
        x = [0]
        y = [self.init_state(100, 100).sum()]
        # self.show()
        for i in range(1, 30):
            y.append(self.sum(1))
            x.append(i)
        # self.show()
        plt.plot(x, y, 'ro')
        plt.show()


def show_list_YP(YP, width=5, height=5):
    for i in range(1, width * height + 1):
        plt.subplot(width, height, i)
        plt.imshow(YP.far_generation(20), cmap='pink', vmin=0, vmax=1)
    plt.show()


def change_r1_w1_YP():
    textname = "../data/save.txt"
    count = 0
    a = np.arange(3, 4, 0.2)
    b = np.arange(0.5, 1.0, 0.1)
    for r1 in a:
        for w1 in b:
            count += 1
            YP = Young_Pattern(r1, r1 * 2, w1, -0.25, 0.08)
            # YP.init_state(50, 50)
            YP.load_text(textname)
            plt.subplot(a.size, b.size, count)
            plt.imshow(YP.far_generation(20), cmap='pink', vmin=0, vmax=1)
    plt.show()


def main():

    YC = Young_Check(3, 6, 1.0, -0.30, 0.08)
    YC.check_plot()
    print(YC.check())

    # change_r1_w1_YP()
    # textname = "../data/save.txt"
    # YP = Young_Pattern(1, 2, 1.0, -0.25, 0.08)
    # # YP.init_state(50, 50)
    # # show_list_YP(YP)
    # YP.init_state(100, 100)
    # YP.load_text(textname)
    # plt.figure(figsize=(10, 10))
    # plt.imshow(YP.far_generation(100), cmap='pink', vmin=0, vmax=1)
    # plt.show()


if __name__ == "__main__":
    main()

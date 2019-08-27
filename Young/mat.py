import matplotlib.pyplot as plt
import numpy as np

from Young.Young_pattern import Young_Pattern


def change_r1_w1_YP():
    a = np.arange(3, 4, 0.2)
    b = np.arange(0.5, 1.0, 0.1)
    fig, ax = plt.subplots(ncols=a.size, nrows=b.size,
                           sharex="col", sharey="all",
                           facecolor="lightgray")
    for aline, r1 in zip(ax, a):
        for elem, w1 in zip(aline, b):
            YP = Young_Pattern(r1, r1 * 2, w1, -0.25, 0.08)
            YP.init_state(50, 50)
            elem.imshow(YP.far_generation(20), cmap='pink')
    plt.show()


def main():
    # fig, ax = plt.subplots(ncols=2, nrows=2,
    #                        sharex="col", sharey="all",
    #                        facecolor="lightgray")
    # print(ax)
    # for aline in ax:
    #     for elem in aline:
    #         elem.plot([1, 2], [0, 1])  # 左上
    # plt.show()
    change_r1_w1_YP()


if __name__ == "__main__":
    main()
    exit()

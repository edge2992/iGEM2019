import matplotlib.pyplot as plt
import numpy as np

from Young.Young_check import Young_Check
from Young.Young_finger import Young_Finger
from Young.Young_pattern import Young_Pattern


def change_w1_w2_YP(a_w1, a_w2):
    gen = 30

    fig, ax = plt.subplots(ncols=a_w2.size, nrows=a_w1.size,
                           sharex="col", sharey="all",
                           facecolor="lightgray")
    fig.suptitle('r1=3 r2=6 w1=xx w2=xx gen={0:.2g}'.format(gen), fontsize=9)
    for aline, w1 in zip(ax, a_w1):
        for elem, w2 in zip(aline, a_w2):
            YP = Young_Finger(3, 6, w1, w2, 0.08)
            # YP.init_state(50, 50)
            elem.imshow(YP.far_generation(gen), cmap='pink')
            elem.set_title("w1={0:.2g} w2={1:.2g}".format(w1, w2), fontsize=7)
    plt.show()


def change_w1_YP(a_w1, w2):
    # w2 = -5.0
    gen = 30

    fig, ax = plt.subplots(ncols=3, nrows=2,
                           sharex="col", sharey="all",
                           facecolor="lightgray")
    fig.suptitle('r1=3 r2=6 w1=xx w2={0:.1f} gen={0:.2g}'.format(w2, gen), fontsize=9)
    count = 0
    for aline in ax:
        for elem, w1 in zip(aline, a_w1):
            YP = Young_Finger(3, 6, a_w1[count], w2, 0.08)
            # YP.init_state(50, 50)
            elem.imshow(YP.far_generation(20), cmap='pink', vmin=0, vmax=1)
            elem.set_title("w1={0:.1f}".format(a_w1[count], fontsize=7))
            count += 1
    plt.savefig('../data/w1_w2-{0:.1f}.png'.format(w2))
    plt.show()


def main():
    filename = "../data/save_big.txt"
    YP = Young_Check(3, 6, 16, -5, 0.08)
    YP.load_text(filename)
    YP.check_plot("small2")

    # a_w1 = np.arange(0.9, 1.2, 0.1)
    # a_w2 = np.arange(-0.4, -0.3, 0.02)
    # change_w1_w2_YP(a_w1, a_w2)

    # change_w1_YP(np.arange(6, 13, 1), -3.0)

    Young_Finger(filename, 3, 6, 16, -5, 0.08).check_plot("rand")


if __name__ == "__main__":
    main()
    exit()



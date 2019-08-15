import numpy as np
import matplotlib.pyplot as plt


def Make_circle(side=20, radius=5):
    grid = np.zeros((side, side))

    a = np.array([(side-1)/2, (side-1)/2])
    for h in range(0, side):
        for w in range(0, side):
            b = np.array([h, w])
            l = np.linalg.norm(b-a)
            # print(h, w, l)
            if l < radius:
                grid[h, w] = 1
    return grid


def Make_around(r1, r2, side=20):
    grid = Make_circle(side, r2)
    grid = grid - Make_circle(side, r1)
    return grid


def main():
    G1 = Make_circle()
    G2 = Make_around(5, 10)

    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1)
    ax1.imshow(G1)
    ax2 = fig.add_subplot(2,1,2)
    ax2.imshow(G2)

    fig.show()


    # plt.subplots(2, 1, 1)
    # plt.imshow(G1)
    # plt.legend()
    #
    # plt.subplots(2, 1, 2)
    # plt.imshow(G2)
    # plt.legend()
    # plt.show()


if __name__ == "__main__":
    main()




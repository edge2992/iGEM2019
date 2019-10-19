import numpy as np
import matplotlib.pyplot as plt


def Make_circle(radius=5, side=20):
    grid = np.zeros((side, side))

    a = np.array([(side - 1) / 2, (side - 1) / 2])
    for h in range(0, side):
        for w in range(0, side):
            b = np.array([h, w])
            l = np.linalg.norm(b - a)
            # print(h, w, l)
            if l < radius:
                grid[h, w] = 1
    return grid


def Make_around(r1, r2, side=20):
    grid = Make_circle(r2, side)
    grid = grid - Make_circle(r1, side)
    return grid


def Make_mask(r1, r2, w1, w2, side=20):
    __grid = np.zeros((side, side))
    __grid += w1 * Make_circle(r1, side)
    __grid += w2 * Make_around(r1, r2, side)
    return __grid


def main():
    G1 = Make_circle()
    G2 = Make_around(5, 10)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.imshow(G1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.imshow(G2)

    fig.show()


if __name__ == "__main__":
    main()

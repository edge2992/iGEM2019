import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt


def make_blank(F, size=50, num=5):
    for i in range(num):
        a = nr.randint(0, F.shape[0] - size - 1)
        b = nr.randint(0, F.shape[0] - size - 1)
        print(a)
        F[a:a + size, b:b + size] = np.zeros((size, size))
    return F


def save(F, dir):
    np.savetxt(dir, F, "%d")
    print("saved it")


def main():
    F = np.loadtxt("../data/save.txt")
    F = make_blank(F, 40, 5)
    plt.imshow(F)
    plt.show()
    # print(type(F))
    np.savetxt("../data/save.txt", F, "%d")
    print("Complete")



if __name__ == '__main__':
    main()


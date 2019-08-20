# 参考
# https://qiita.com/sage-git/items/c6c175887faa4cf737fb
# opencvで描画する

import sys
import numpy as np
from scipy import signal
import cv2

from dots import Make_circle, Make_around

mask_inner = Make_circle(side=21, radius=3)
mask_outer = Make_around(3, 6)

mask = np.ones((4, 4), dtype=int)

w1 = 1.0
w2 = -0.3


def init_state(width, height, init_alive_prob=0.5):
    N = width*height
    v = np.array(np.random.rand(N) + init_alive_prob, dtype=int)
    return v.reshape(height, width)


def count_inner_neighbor(F):
    return count_neighbor(F, mask_inner)


def count_outer_neighbor(F):
    return count_neighbor(F, mask_outer)


def count_neighbor(F, mask_type):
    return signal.correlate2d(F, mask_type, mode="same", boundary="wrap")

# def count_neighbor(F):
#     return signal.correlate2d(F, mask, mode="same", boundary="wrap")


def next_generation(F):
    # N = count_neighbor(F)
    # # G = np.array(N == 3, dtype=int) + F * np.array(N == 4, dtype=int)
    # G = (N == 3) + F * (N == 4)
    N = count_inner_neighbor(F) * w1 + count_outer_neighbor(F) * w2
    G = N > 0
    return G


def to_image(F, scale=3.0):
    img = np.array(F, dtype=np.uint8)*255
    W = int(F.shape[1]*scale)
    H = int(F.shape[0]*scale)
    img = cv2.resize(img, ((int)(W/2), (int)(H/2)), interpolation=cv2.INTER_NEAREST)
    return img


def main():
    p = 0.08
    F = init_state(300, 300, init_alive_prob=p)
    ret = 0
    wait = 50
    while True:
        img = to_image(F, scale=5.0)
        cv2.imshow("test", img)
        ret = cv2.waitKey(wait)
        F = next_generation(F)
        if ret == ord('r'):
            F = init_state(300, 300, init_alive_prob=p)
        if ret == ord('s'):
            wait = min(wait*2, 1000)
        if ret == ord('f'):
            wait = max(wait//2, 10)
        if ret == ord('q') or ret == 27:
            break
        if ret == ord('w'):
            np.savetxt("../data/save.txt", F, "%d")
        if ret == ord('l'):
            if cv2.os.path.exists("../data/save.txt"):
                F = np.loadtxt("../data/save.txt")
    cv2.waitKey() #macの都合
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()




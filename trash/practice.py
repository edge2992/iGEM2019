# training for open CV
# 数える練習
# 参考
# https://qiita.com/sage-git/items/c6c175887faa4cf737fb
import sys
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


#初期値
width = 10
height = 10
init_alive_prob = 0.5


N = width*height
v = np.array(np.random.rand(N) + init_alive_prob, dtype=int)
F = v.reshape(height, width)

mask = np.ones((3, 3), dtype=int)
signal.correlate2d(F, mask, mode="same", boundary="wrap")

print("F")
np.savetxt(sys.stdout.buffer, F, fmt="%d")
print('\nsignal.correlate2d(F, mask, mode="same", boundary="wrap")')
np.savetxt(sys.stdout.buffer, signal.correlate2d(F, mask, mode="same", boundary="wrap"), fmt="%d")






# from yasuda
# https://vigne-cla.com/17-5/

import numpy as np
import numpy.random as nr
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import animation, rc

# ============================
# 初期状態の設定
# ============================

# 高さ、幅
h, w = 100, 100

# 終了ステップ数
max_step = 10000

# 拡散係数
D1 = 0.2
D2 = 0.1

# キリン模様
start = 1  # 0:中央のみ、1:複数
f = 0.082
k = 0.059

# 伸びる線
# start = 1 #0:中央のみ、1:複数
# f = 0.058
# k = 0.065

# 線の生成
# start = 0 #0:中央のみ、1:複数
# f = 0.046
# k = 0.063

# 線といくらの生成
# start = 0 #0:中央のみ、1:複数
# f = 0.034
# k = 0.0618

# いくらウロウロ
# start = 1 #0:中央のみ、1:複数
# f = 0.014
# k = 0.054

# タピオカカオス
# start = 1 #0:中央のみ、1:複数
# f = 0.0353
# k = 0.0566

# 細胞分裂
# start = 0 #0:中央のみ、1:複数
# f = 0.030
# k = 0.063

# 細胞分裂パルス
# start = 0 #0:中央のみ、1:複数
# f = 0.022
# k = 0.059

# 波
# start = 1 #0:中央のみ、1:複数
# f = 0.0159
# k = 0.045

# ============================
# メイン処理
# ============================

# フィールドの初期化
u = np.ones((h, w))
v = np.zeros((h, w))

# 初期状態の設定
size = 6
if start == 0:
    # 中央に乱数の正方形
    u[h // 2 - size // 2:w // 2 + size // 2, h // 2 - size // 2:w // 2 + size // 2] = nr.rand(size, size)
    v[h // 2 - size // 2:w // 2 + size // 2, h // 2 - size // 2:w // 2 + size // 2] = nr.rand(size, size)
if start == 1:
    # ランダムな位置に複数の乱数正方形
    for i in range(20):
        p = (nr.randint(size, h - size), nr.randint(size, w - size))
        u[p[0] - size // 2:p[0] + size // 2, p[1] - size // 2:p[1] + size // 2] = nr.rand(size, size)
        v[p[0] - size // 2:p[0] + size // 2, p[1] - size // 2:p[1] + size // 2] = nr.rand(size, size)

# 畳み込み用のフィルタ
g = np.array([[0.00, 1.00, 0.00],
              [1.00, -4.0, 1.00],
              [0.00, 1.00, 0.00]])

# 画像をスタックする配列の準備
fig = plt.figure()
# fig = plt.figure(figsize=(10, 10))
ims = []

# 初期状態の表示（スタック）
im = plt.imshow(u, cmap='pink', vmin=0, vmax=1)
ims.append([im])

# 状態の更新
for i in range(1, max_step + 1):

    # 拡散項（u, vを畳み込んでdu, dvとする）
    du = signal.convolve2d(u, g, mode='same', boundary='wrap') * D1
    dv = signal.convolve2d(v, g, mode='same', boundary='wrap') * D2

    # du, dvに反応項を加える
    du = du - (u * v * v) + f * (1.0 - u)
    dv = dv + (u * v * v) - (f + k) * v

    # フィールドの更新（オイラー法）
    u += du
    v += dv

    # 表示（スタック）
    if i % 100 == 0:
        im = plt.imshow(u, cmap='pink', vmin=0, vmax=1)
        ims.append([im])

# アニメーション表示の準備
print('making animation......')
print('len(ims) = ' + str(len(ims)))
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)

# ここにアニメを表示する場合はこちらを有効に
rc('animation', html='jshtml')
ani

# .gifや.mp4を保存する場合はこちらを有効に
# ani.save('aaa.gif', writer='imagemagick',fps=40)
# ani.save('bbb.mp4', writer="ffmpeg")
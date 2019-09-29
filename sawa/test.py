import cv2

from Young.Young_finger import Young_Finger
from nakano.image_processing import load_image_grayscale, thinning, blur, threshold, morphological_transformations
from nakano.width_getter import get_width
import numpy as np

# いままでのfingerprint.pngを調べてみると幅の最頻値は8になった
# r1 = 3, r2 = 6の時のランダムでの最頻値は10であることから
# ある程度幅をもってパターンを作ることが分かった。

# filename = "../picture_edit/img/fingerprint.png"
filename = "../features_detection/fingerprint.png"
YF = Young_Finger(3, 6, 15, -5)
img = load_image_grayscale(filename)
img_edited = blur(img)
img_edited = threshold(img_edited)
img_edited = morphological_transformations(img_edited)
# img = cv2.resize(img, dsize=None, fx=1.3, fy=1.3)
print(img_edited.shape)
thined = thinning(img_edited)

width = get_width(thined)
print("画像の最頻値(幅): " + str(width))  # 元の幅
xx = 8.5 / width
print("倍率: " + str(xx))


resized = cv2.resize(img, dsize=None, fx=xx, fy=xx)
resized = threshold(resized)

YF.load_ndarray(resized)
YF.r_rd = 10
YF.far_generation(1)
YF.show()
# YF.show_cv2()
YF.far_generation(10)
YF.show()
img2 = YF.state.astype(np.uint8)
img2 = img2 * 255
thined2 = thinning(img2)
width2 = get_width(thined2)
print("パターン生成後の最頻値(幅): " + str(width2))  # パターン生成後の幅

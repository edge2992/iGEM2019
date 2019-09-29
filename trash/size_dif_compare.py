import traceback

import numpy as np
import matplotlib.pyplot as plt

from Image_Comparison.compare import compare_two_from_cv2
from Young.Young_finger import Young_Finger

size = np.array([300, 350, 400, 450, 500, 500])

fig, ax = plt.subplots(ncols=3, nrows=2,
                       sharex="col", sharey="all",
                       facecolor="lightgray")
count = 0
r1 = 3
r2 = 6
w1 = 12
w2 = -3.0
gen = 30
for aline in ax:
    for elem in aline:
        filename = "../picture_edit/img_size/finger01_{0:.3g}.txt".format(size[count])
        YP = Young_Finger(filename, r1, r2, w1, w2)
        initial_IMG = YP.to_image()
        # 世代を進める
        YP.far_generation(gen)
        opt_IMG = YP.to_image()

        # 出力用
        elem.imshow(YP.state, cmap='pink', vmin=0, vmax=1)
        elem.set_title("size={0:.1f}".format(size[count], fontsize=7))

        # 比較
        # try:
        #     print("size={0:.3g} PSNR".format(size[count]))
        #     print(compare_two_from_cv2(initial_IMG, opt_IMG))
        # except:
        #     print("error")
        #     traceback.print_exc()

        count += 1

plt.savefig("sizedif.png")
plt.show()


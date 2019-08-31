import numpy as np

from picture_edit.mosaic_pic import Mosaic

image = "img/fingerprint.png"
size = np.array([300, 350, 400, 450, 500])

for width in size:
    Mos = Mosaic(width, width)
    Mos.mosaic(image)
    Mos.save("img_size/finger01_{0:.3g}.txt". format(width))

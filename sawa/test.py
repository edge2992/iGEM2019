import logging
from datetime import datetime
from logging import getLogger, DEBUG, StreamHandler

import cv2

from Young.Young_finger import Young_Finger
from Young.Young_pattern import Young_Pattern
from nakano import image_processing
from nakano.image_processing import load_image_grayscale, thinning, blur, threshold, morphological_transformations, \
    image_show
from nakano.width_getter import get_width
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def trim(img, left=0., right=1., top=0., bottom=1., debug=False):
    """
    トリミングする
    :param debug:
    :param img: 0~1
    :param left: 0~1
    :param right: 0~1
    :param top: 0~1
    :param bottom: 0~1
    :return:
    """
    if debug:
        print("start: trim")
    height = img.shape[0]
    width = img.shape[1]

    if (left > right) or (top > bottom):
        print("left & top should be lower than right & bottom")
    elif (0 > left) and (left > 1):
        print("parameter left should be 0 to 1")
    elif (0 > right) and (right > 1):
        print("parameter right should be 0 to 1")
    elif (0 > top) and (top > 1):
        print("parameter top should be 0 to 1")
    elif (0 > bottom) and (bottom > 1):
        print("parameter bottom should be 0 to 1")
    else:
        result = img[int(height * top):int(height * bottom), int(width * left):int(width * right)]
        if debug:
            image_show(img, "trim - before")
        if debug:
            image_show(result, "trim - after")
        if debug:
            print("end  : trim")
        return result


def gif_maker(YP, generation=20, duration=300,
              img_path="./image-" + str(int(datetime.now().timestamp() * (10 ** 3))) + ".gif"):
    """
    gif画像を作る
    :param generation:
    :param img_path:
    :param duration:
    :type YP: Young_Pattern
    """
    ims = []

    fig = plt.figure(figsize=(3, 3))
    plt.imshow(YP.state)
    fig.canvas.draw()

    image_array = np.array(fig.canvas.renderer.buffer_rgba())
    im = Image.fromarray(image_array)
    ims.append(im)
    plt.close()

    for i in range(generation):
        # 描画
        fig = plt.figure(figsize=(3, 3))
        plt.imshow(YP.next_generation())
        fig.canvas.draw()

        image_array = np.array(fig.canvas.renderer.buffer_rgba())
        im = Image.fromarray(image_array)
        ims.append(im)
        plt.close()

    ims[0].save(img_path, save_all=True, append_images=ims[1:], loop=0, duration=duration)


# いままでのfingerprint.pngを調べてみると幅の最頻値は8になった
# r1 = 3, r2 = 6の時のランダムでの最頻値は10であることから
# ある程度幅をもってパターンを作ることが分かった。

PRINT = 1
GIF = 2
PNG = 3

logger = getLogger(__name__)
logger.setLevel(DEBUG)
StreamHandler().setLevel(DEBUG)
logger.addHandler(logging.StreamHandler())


def Optimal_Pattern(file_path="../picture_edit/img/fingerprint.png",
                    save_path = "./image-" + str(int(datetime.now().timestamp() * (10 ** 3))),
                    generation=10, true_width = 9.5, YP=Young_Finger(3, 6, 15, -5), mode=PRINT):
    """
    幅をあわせて指紋を修復する
    :param save_path:
    :param generation: int
    :param mode:
    :param file_path:
    :type YP: Young_Pattern
    """
    logger.info("Optimal_pattern start")

    # imageの幅を図る
    img = image_processing.load_image_grayscale(file_path)
    img_edited = image_processing.blur(img)
    img_edited = image_processing.threshold(img_edited)
    # img_edited = image_processing.bitwise_not(img_edited)
    img_edited = image_processing.morphological_transformations(img_edited)
    thined = image_processing.thinning(img_edited)
    width = get_width(thined)
    logger.debug("最頻値(幅): " + str(width))
    magnify = true_width / width
    logger.debug("倍率: " + str(magnify))

    # その倍率で拡大する
    resized = cv2.resize(img, dsize=None, fx=magnify, fy=magnify)
    resized = image_processing.threshold(resized)
    # デフォルトの縮尺に合わせている
    trimed = trim(resized, 0.05, 0.9, 0.1, 0.9, True)
    YP.load_ndarray(trimed)
    if mode == PRINT:
        YP.far_generation(generation)
        YP.show()
    elif mode == GIF:
        gif_maker(YP, generation=generation, duration=1000, img_path=save_path+".gif")
    elif mode == PNG:
        YP.far_generation(generation)
        YP.save_img(img_path=save_path+".png")

    logger.debug("Optimal_pattern end")


if __name__ == "__main__":
    # logger.basicConfig(level=logging.DEBUG)
    # Optimal_Pattern(mode=GIF, save_path="rand_example")
    Optimal_Pattern(mode=GIF, true_width=6, save_path="bad_example")
    # Optimal_Pattern(mode=GIF, YP=Young_Pattern(3, 6, 15, -5), save_path="not_rand_fingerprint")
    # exit()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import random
import sys

if __name__ == '__main__':

    # 対象画像を指定
    input_image_path = 'img/fingerprint.png'

    # 画像をグレースケールで読み込み
    gray_src = cv2.imread(input_image_path, 0)
    if gray_src is None:
        # 読み込みに失敗した場合は None が返る。
        print('failed to load image.')

    # 前処理（平準化フィルターを適用した場合）
    # 前処理が不要な場合は下記行をコメントアウト
    # blur_src = cv2.GaussianBlur(gray_src, (5, 5), 2)

    # 二値変換
    # 前処理を使用しなかった場合は、blur_srcではなくgray_srcに書き換えるする
    mono_src = cv2.adaptiveThreshold(gray_src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)

    # 結果の表示
    cv2.imshow("mono_src", mono_src)

    cv2.waitKey(0)
    cv2.destroyAllWindows()




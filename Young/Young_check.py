import cv2

from Young.Young_pattern import Young_Pattern
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


BackendError = type('BackendError', (Exception,), {})


def is_visible(winname):
    # cv2の閉じるエラーを解決したい（未解決）
    try:
        ret = cv2.getWindowProperty(
            winname, cv2.WND_PROP_VISIBLE
        )

        if ret == -1:
            raise BackendError('Use Qt as backend to check whether window is visible or not.')

        return bool(ret)

    except cv2.error:
        return False


class Young_Check(Young_Pattern):
    # Todo: チューリングパターンをパラメーターごとに一覧表示
    def __init__(self, r1, r2, w1, w2, init_alive_prob=0.5):
        super(Young_Check, self).__init__(r1, r2, w1, w2, init_alive_prob)

    def sum(self, generation=2):
        """
        stateの1の数を足す
        :param generation:
        :return:
        """
        C = self.far_generation(generation)
        return C.sum()

    def check(self, width=100, height=100, generation=30):
        """
        黒の部分の割合をだす（0~1）
        :param width: stateの横幅
        :param height: stateの縦幅
        :param generation: 何世代後？
        :return:
        """
        self.init_state(width, height)
        num = self.sum(generation)
        # return width * height * 0.9 > num > width * height * 0.1
        return num * 1.0 / (width * height)

    def show_ini_end(self, filename,  gen=30):
        fig, ax = plt.subplots(ncols=2,
                               sharex="col", sharey="all",
                               facecolor="lightgray")
        fig.suptitle('r1={0:.2g} r2={1:.2g} w1={2:.2g} w2={3:.2g} gen={4:.2g}'.format(self.r1, self.r2, self.w1, self.w2, gen), fontsize=9)
        ax[0].imshow(self.init_state(), cmap='pink')
        ax[0].set_title("initial state ", fontsize=7)
        ax[1].imshow(self.far_generation(gen), cmap='pink')
        ax[1].set_title("generation={0:.2g} ".format(gen), fontsize=7)
        plt.savefig("../data/compare_" + filename + ".png")
        plt.show()

    def check_plot(self):
        """
        plotを出力して収束を確認する
        """
        x = [0]
        # y = [self.init_state(100, 100).sum()]
        y = [self.state.sum()]
        # self.show()
        for i in range(1, 30):
            y.append(self.sum(1))
            x.append(i)
        # self.show()
        plt.plot(x, y, 'ro')
        plt.show()

    def show_cv2(self):
        winname = "Young Pattern"
        # ret = 0
        wait = 50

        while True:
            img = self.to_image()
            cv2.imshow(winname, img)
            ret = cv2.waitKey(wait)
            self.next_generation()
            # prop_val = cv2.getWindowProperty(winname, cv2.WND_PROP_ASPECT_RATIO)
            if ret == ord('r'):
                self.init_state(init_alive_prob=0.08)
            if ret == ord('s'):
                wait = min(wait * 2, 1000)
            if ret == ord('f'):
                wait = max(wait // 2, 10)
            if ret == ord('q') or ret == 27:
                break
            if not is_visible(winname):
                break
            if ret == ord('w'):
                self.save_text("../data/save.txt")
            if ret == ord('l'):
                self.load_text("../data/save.txt")
        cv2.waitKey(1)  # macの都合
        cv2.destroyAllWindows()
        return 0


def heat_map(para1_name, para1, para2_name, para2):
    """
    ヒートマップを作成する関数
    :param para1_name: パラメータの名前
    :param para1: 実験するパラメーターの幅のarray
    :param para2_name: パラメータの名前
    :param para2: 実験するパラメーターの幅のarray
    :return:
    """
    pd.options.display.float_format = '{:.1f}'.format
    pd.options.display.float_format = '{:.1f}'.format
    param_df = ({'r1': 3,
                 'r2': 6,
                 'w1': 1.0,
                 'w2': -0.3,
                 'init_alive_prob': 0.08})

    df = pd.DataFrame({para1_name: [],
                       para2_name: [],
                       'score': []})

    for aa in para1:
        for bb in para2:
            param_df[para1_name] = aa
            param_df[para2_name] = bb
            tmp_se = pd.Series([aa, bb,
                                Young_Check(param_df['r1'], param_df['r2'], param_df['w1'], param_df['w2'],
                                            param_df['init_alive_prob']).check(25, 25)],
                               index=[para1_name, para2_name, 'score'])
            df = df.append(tmp_se, ignore_index=True)
    print(df)

    print(type(param_df['w1']))
    df_pivot = pd.pivot_table(data=df, values='score',
                              columns=para1_name, index=para2_name, aggfunc=np.mean)
    sns.heatmap(df_pivot, cmap='Blues', annot=False)
    # sns.heatmap(df_pivot, cmap='Blues', annot=True, fmt='.2f')
    # plt.gca().xaxis.set_major_formatter(plt.ScalarFormatter(useMathText=True))
    plt.title('r1={0:.2g} r2={1:.2g} w1=xx w2=xx gen={2:.2g}'.format(3, 6, 30), fontsize=9)
    plt.savefig('../data/' + para1_name + '_' + para2_name + '.png')
    plt.show()

    plt.close('all')
    return df


def show_list_YP(YP, width=5, height=5):
    for i in range(1, width * height + 1):
        plt.subplot(width, height, i)
        plt.imshow(YP.far_generation(20), cmap='pink', vmin=0, vmax=1)
    plt.show()


def change_r1_w1_YP():
    gen = 30
    a = np.arange(3, 6, 1)
    b = np.arange(0.9, 1.3, 0.1)
    fig, ax = plt.subplots(ncols=b.size, nrows=a.size,
                           sharex="col", sharey="all",
                           facecolor="lightgray")
    fig.suptitle('r1=xx r2=r1*2 w1=xx w2={0:.2g} gen={1:.2g}'.format(-0.3, gen), fontsize=9)
    for aline, r1 in zip(ax, a):
        for elem, w1 in zip(aline, b):
            YP = Young_Pattern(r1, r1 * 2, w1, -0.25, 0.08)
            YP.init_state(50, 50)
            elem.imshow(YP.far_generation(gen), cmap='pink')
            elem.set_title("r1={0:.2g} w1={1:.2g}".format(r1, w1), fontsize=7)
    plt.show()


def main():
    YP = Young_Check(3, 6, 16.0, -5.0, 0.08)
    YP.show_ini_end()
    # heat_map('w1', np.arange(0, 30, 0.5), 'w2', np.arange(-10.0, 0., 0.5))
    # change_r1_w1_YP()


if __name__ == "__main__":
    main()
    exit()

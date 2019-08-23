from Young.Young_pattern import Young_Pattern
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


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

    def check_plot(self):
        """
        plotを出力して収束を確認する
        """
        x = [0]
        y = [self.init_state(100, 100).sum()]
        # self.show()
        for i in range(1, 30):
            y.append(self.sum(1))
            x.append(i)
        # self.show()
        plt.plot(x, y, 'ro')
        plt.show()


def heat_map(para1_name, para1, para2_name, para2):
    """
    ヒートマップを作成する関数
    :param para1_name: パラメータの名前
    :param para1: 実験するパラメーターの幅のarray
    :param para2_name: パラメータの名前
    :param para2: 実験するパラメーターの幅のarray
    :return:
    """
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
            # print(param_df.values)
            tmp_se = pd.Series([aa, bb,
                                Young_Check(param_df['r1'], param_df['r2'], param_df['w1'], param_df['w2'],
                                            param_df['init_alive_prob']).check(25, 25)],
                               index=[para1_name, para2_name, 'score'])
            df = df.append(tmp_se, ignore_index=True)
    print(df)
    df_pivot = pd.pivot_table(data=df, values='score',
                              columns=para1_name, index=para2_name, aggfunc=np.mean)
    sns.heatmap(df_pivot, cmap='Blues', annot=True)
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
    textname = "../data/save.txt"
    count = 0
    a = np.arange(3, 4, 0.2)
    b = np.arange(0.5, 1.0, 0.1)
    for r1 in a:
        for w1 in b:
            count += 1
            YP = Young_Pattern(r1, r1 * 2, w1, -0.25, 0.08)
            # YP.init_state(50, 50)
            YP.load_text(textname)
            plt.subplot(a.size, b.size, count)
            plt.imshow(YP.far_generation(20), cmap='pink', vmin=0, vmax=1)
    plt.show()


def main():
    heat_map('w1', np.arange(0.7, 1.3, 0.1), 'w2', np.arange(-0.5, -0., 0.1))

    # change_r1_w1_YP()
    # textname = "../data/save.txt"
    # YP = Young_Pattern(1, 2, 1.0, -0.25, 0.08)
    # # YP.init_state(50, 50)
    # # show_list_YP(YP)
    # YP.init_state(100, 100)
    # YP.load_text(textname)
    # plt.figure(figsize=(10, 10))
    # plt.imshow(YP.far_generation(100), cmap='pink', vmin=0, vmax=1)
    # plt.show()


if __name__ == "__main__":
    main()

from datetime import datetime

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Young.Young_pattern import Young_Pattern
import numpy as np


def r12_heatmap(rr1, rr2):
    """
    r1\r2のヒートマップを作成する
    :param rr1: ndarray
    :param rr2:
    """
    df_pivot = __heat_map("r1", rr1, "r2", rr2)

    sns.heatmap(df_pivot, cmap='Blues', annot=True)
    plt.title('r1=xx r2=xx w1={0:.2g} w2={1:.2g} gen={2:.2g}'.format(16, -5, 10), fontsize=9)
    plt.savefig("r1_r2_search" + str(int(datetime.now().timestamp() * (10 ** 3))) + ".png")
    plt.show()

    plt.close('all')


def w12_heatmap(ww1, ww2):
    """
    w1/w2のヒートマップを作成する
    :param ww1:
    :param ww2:
    """
    df_pivot = __heat_map("w1", ww1, "w2", ww2)

    sns.heatmap(df_pivot, cmap='Blues', annot=False)
    plt.title('r1={0:.2g} r2={1:.2g} w1=xx w2=xx gen={2:.2g}'.format(3, 6, 10), fontsize=9)
    plt.savefig("w1_w2_search" + str(int(datetime.now().timestamp() * (10 ** 3))) + ".png")
    plt.show()

    plt.close('all')


def __heat_map(para1_name, para1, para2_name, para2):
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
                 'w1': 16.0,
                 'w2': -5.0,
                 'init_alive_prob': 0.08})

    df = pd.DataFrame({para1_name: [],
                       para2_name: [],
                       'score': []})

    for aa in para1:
        for bb in para2:
            param_df[para1_name] = aa
            param_df[para2_name] = bb
            YP = Young_Pattern(param_df['r1'], param_df['r2'], param_df['w1'], param_df['w2'])
            YP.init_state(25, 25)
            result = YP.far_generation(10).sum() / (YP.width * YP.height)
            tmp_se = pd.Series([aa, bb, result], index=[para1_name, para2_name, 'score'])
            df = df.append(tmp_se, ignore_index=True)
    print(df)

    print(type(param_df['w1']))
    df_pivot = pd.pivot_table(data=df, values='score',
                              columns=para1_name, index=para2_name, aggfunc=np.mean)
    return df_pivot


# r12_heatmap(np.arange(1, 7), np.arange(1, 16))

w12_heatmap(np.arange(0, 30, 0.5), np.arange(-10.0, 0., 0.5))

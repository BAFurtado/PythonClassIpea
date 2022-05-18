import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import statsmodels.api as sm


def prepare_data(data):
    y = data.success.astype(int)
    dummies = pd.get_dummies(data, columns=['strategy', 'goal'])
    # Getting baselines:
    # For Strategy: Base is Minimalist.
    # For Goal: Base is Territory18.
    include = ['strategy_blitz', 'strategy_sensible', 'goal_continent', 'goal_territory24', 'goal_destroy']
    x = pd.concat([data.luck.astype(float), dummies[include].astype(int)], axis=1)
    # Numpy array
    return x.to_numpy(), y.to_numpy(), ['luck'] + include


def regress(x, y, cols):
    lm = sm.Logit(y, x)
    pm = sm.Probit(y, x)
    res_lm = lm.fit()
    # res_pm = pm.fit()
    print(res_lm.summary2(yname='Success', xname=cols, title='Logit Regression'))
    # print(res_pm.summary2(yname='Success', xname=cols, title='Probit Regression'))

    return res_lm, lm


if __name__ == "__main__":
    d = pd.read_csv('data/reg_0.csv', sep=';')
    X, Y, C = prepare_data(d)
    res, l = regress(X, Y, C)

    # More processing results
    head_details = pd.read_html(res.summary(yname='Success', xname=C).tables[0].as_html(), header=0, index_col=0)[0]
    results_body = pd.read_html(res.summary(yname='Success', xname=C).tables[1].as_html(), header=0, index_col=0)[0]
    head2 = pd.read_html(res.summary2(yname='Success', xname=C).as_html())[0]

    # with open(f'results/results_reg_bundle', 'wb') as f:
    #     pickle.dump([head_details, results_body, head2], f)

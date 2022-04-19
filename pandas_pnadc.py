import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Good piece on GROUPBY: https://towardsdatascience.com/pandas-groupby-aggregate-transform-filter-c95ba3444bbb


def read_basics(path):
    data = pd.read_csv(path, sep=';')
    return data


def weighted_avg(data, by, values, weights):
    group = data.groupby(by)
    data[f'{values}_med'] = data[values] / group[values].transform("sum") * data[weights]
    return data


def weighted_avg_np(data, by, value, weights):
    return data.groupby(data[by]).apply(lambda x: np.average(data[weights], weights=data[value]))


if __name__ == '__main__':
    p = 'data/pnadc2020.csv'
    d = read_basics(p)
    renda_med = weighted_avg(d, 'domicilioid', 'renda_trabalho_habitual', 'peso')
    renda_med_n2 = np.average(d['renda_trabalho_habitual'], weights=d['peso'])
    # renda_med_n2_gr = d.groupby(['domicilioid']).apply(lambda x: np.average(x['renda_trabalho_habitual'],
                                                                              #  weights=x['peso']))

    print(renda_med.groupby('uf').agg('mean')['renda_trabalho_habitual_med'])
    print(renda_med.groupby(['trimestre', 'uf']).agg('mean')['renda_trabalho_habitual_med'])
    renda_med.groupby(['trimestre']).agg('mean')['renda_trabalho_habitual_med'].plot()
    plt.show()
    #
    by_sex = renda_med.groupby(['trimestre', 'sexo']).agg('mean').reset_index()
    for each in by_sex['sexo'].unique():
        plt.plot(by_sex['trimestre'].unique(), by_sex[by_sex['sexo'] == each]['renda_trabalho_habitual_med'])
    plt.show()


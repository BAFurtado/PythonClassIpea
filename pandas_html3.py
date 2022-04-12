import matplotlib.pyplot as plt
import pandas as pd

# 0. Iterating over a groupby
# 1. List comprehension


# Tarefas:
# 1. Quantos dias em média entre o pedido (OrderDate) e a postagem (ShipDate). Use pd.to_datetime(column).
# Faça a diferença.
# 2. Faça uma frequencia (value_counts) da coluna ShipStatus
# 3. Some o Profit por State e ordene. California lucrou mais? E o segundo?
# 4. Quais são as 4 categorias de envio (ShipMode)? Qual é o mais lucrativo?


def direto_csv_net(address):
    return pd.read_csv(f'{address}?raw=True')


if __name__ == '__main__':
    p2 = r'https://github.com/metatron-app/metatron-doc-discovery/blob/master/_static/data/sales-data-sample.csv'
    d2 = direto_csv_net(p2)
    d2.plot('longitude', 'latitude', kind='scatter')
    plt.show()
    # d3 = d2.groupby('ShipMode').agg(['sum', 'count'])['Profit']

    # print(len(d2))
    # for name, grupo in d2.groupby('ShipMode'):
    #     print(name, type(grupo), len(grupo))

    # gr = [g for n, g in d2.groupby('ShipMode')]

    import math


    class Foo:
        def __init__(self, i):
            self.i = i

        def raiz(self):
            self.i = math.sqrt(self.i)

    a = [1, 2, 3, 4]
    [math.sqrt(i) for i in a]
    b = [Foo(i) for i in a]
    [i.raiz() for i in b]

    b[1].i

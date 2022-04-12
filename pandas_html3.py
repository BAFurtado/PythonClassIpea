import matplotlib.pyplot as plt
import pandas as pd

# 0. Iterating over a groupby
# 1. List comprehension. Dictionary comprehension
# {k: += for k in range(5)}


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
            # Não temos um return nessa função
            # Logo, por padrão, python sempre retorna None

    a = [1, 2, 3, 4]
    [math.sqrt(i) for i in a]
    b = [Foo(i) for i in a]
    [i.raiz() for i in b]

    b[1].i

    lista_nova = list()
    for i in range(10):
        lista_nova.append(i)

    lista_nova2 = [i for i in range(10)]

    a = {'a': 100, 'b': 200}

    # dicionários, por padrão, o loop é na chave
    # vc pode usar explícito. dict.keys()
    # pode-se usar os valroes dict.values()
    # ou ambos: dict.items()
    for k, v in a.items():
        print(k)
        print(v ** 2)

    lista_nova = list()
    for i in range(10):
        if i > 5:
            lista_nova.append(i)

    # se a condicional contiver um ELSE, é necessário trazer toda a
    # expressão para antes do for (loop)
    lista_nova2 = [math.sqrt(i) if i > 5 else 0 for i in range(10)]




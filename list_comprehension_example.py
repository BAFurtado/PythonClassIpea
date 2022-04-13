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

print(b[1].i)

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

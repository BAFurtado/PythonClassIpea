""" Exemplo de histogramas usando dicionários.
    Adaptado de Think Python. Chapter 11

"""
import lists_generator

print('Introducing dictionary method .get(key, default values')
print(dict().get)
print('')

""" To illustrate the process, try to add a value to a key that does not exist.
    e = dict() 
    e['nokey'] = e['nokey'] + 1
    What happens?
    """


def histogram(data):
    d = dict()
    for each in data:
        d[each] = d.get(each, 0) + 1
    return d


if __name__ == '__main__':
    string1 = 'paralelepipedo'
    d1 = histogram(string1)
    print(string1)
    print(d1)
    print('')
    l3 = lists_generator.generate()
    d2 = histogram(l3)
    print(f'lista aleatória {l3}')
    print(d2)

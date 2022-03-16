


import json
import os
from collections import defaultdict


def my_database(k: str, d: dict) -> dict:
    """ Class example to create and maintain a persistent database
        using JSON and dictionaries
        Recebe como parâmetros, uma chave (nome, por exemplo) e um dicionário]
        com as informações acessarem acrescentadas.
        Salva num JSON.
    """
    # Checking if database exists
    if os.path.exists('my_database.json'):
        with open('my_database.json', 'r') as f:
            data = json.load(f)
    # If not saved before, create dictionary for the first time
    else:
        # Prepara o dicionário para receber outros dicionários como valores
        data = defaultdict(dict)

    # Adding data to the dictionary
    data.update({k: d})

    # Saving it in file
    with open('my_database.json', 'w') as f:
        json.dump(data, f)

    print('Current dictionary is: \n{}'.format(data))
    return data


if __name__ == '__main__':
    # JSON -->  use code -> reformat file
    key = 'Bianca'
    new_dict_value = {'age': 36, 'cargo': 'advogado', 'salario': 1680}
    d = my_database(key, new_dict_value)

    key = 'Fredegonda'
    value = {'local': 'Fargo, Montana', 'cargo': 'nem-nem', 'salario': 15}
    d = my_database(key, value)

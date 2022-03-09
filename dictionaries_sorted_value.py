""" Sort dictionaries by value
"""


def sort_by_value(data: dict) -> list:
    return sorted(data.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)


if __name__ == '__main__':
    d = {'a': 0, 'b': 1, 'c': 14, 'd': 12}
    print(sort_by_value(d))

    # Mais exemplos
    exemplo_tuples = [(1, 2, 3), (7, 7, 4), (9, 0, 1), (100, 70, 2000)]
    print(sorted(exemplo_tuples, key=lambda x: x[2]))

    exemplo_2 = [(1, 2, 3), (9, 7, 2), (9, 0, 6), (-100, 70, 2000)]
    print(sorted(exemplo_2, key=lambda x: (abs(x[0]), x[1]), reverse=True))


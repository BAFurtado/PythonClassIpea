
print('helloo')


def mult_two(a, b):
    return a * b


if __name__ == '__main__':
    resultado = mult_two(10, 2)
    print(resultado)
    assert mult_two(2, 2) == 4

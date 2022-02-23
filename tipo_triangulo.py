

def triangulo(lados: list) -> str:
    if len(lados) != 3:
        return
    a = lados[0]
    b = lados[1]
    c = lados[2]
    if a == b == c:
        return 'equilatero'
    elif (a == b) or (b == c) or (a == c):
        return 'isosceles'
    else:
        return 'escaleno'


if __name__ == '__main__':
    eq = [4, 4, 4]
    iso = [4, 4, 7]
    escal = [3, 4, 5]
    print(triangulo(eq))
    print(triangulo(iso))
    print(triangulo(escal))

    assert triangulo(eq) == 'equilatero'
    assert triangulo(iso) == 'isosceles'
    assert triangulo(escal) == 'escaleno'

    teste = [1, 2, 3, 4]
    triangulo(teste)


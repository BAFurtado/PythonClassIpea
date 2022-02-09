""" Script que calcula a área do círculo
    Exemplo de função comentada
    Adapted from Python for ABM 2019 into 2022
    """

""" Eu uso tres aspas para
    comentar ultrapassando mais 
    de uma linha, sem problemas
    """

import math

import function5


def area_circle(r):
    """ Função que calcula área do círculo.
        Parâmetro: r - o raio do círculo
        Retorna a área
        """
    # Jogo da velha é usado para comentários de uma linha só.
    # Este código não é rodado (evaluated). x = 1000
    # y = 1000
    # Fórmula área
    area = math.pi * r ** 2
    return area


""" Running the module individually.
    Quando este módulo (script/library) importado, o código abaixo do main
    não roda
    """
if __name__ == '__main__':
    raio = 2
    result = area_circle(raio)
    # Exemplo de formatação de output com float e duas casas decimais usando format
    print(f'A área é: {result:.2f}')

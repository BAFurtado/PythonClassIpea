""" From Think Python by Allen Doyne p. 26
Exercise 3.1. Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the string is in column 70
of the display.

"""


def right_justify(word):
    print(f"{' ' * (70 - len(word))}{word}")


if __name__ == '__main__':
    print(f'este texto sempre é impresso e o que vem entre '
          f'chaves é avaliado: {2 ** 3}')
    right_justify('meu')
    # A última letra tem que estar na mesma posição final da palavra inicial
    right_justify('primeiro')
    right_justify('poema')
    right_justify('concreto')
    print(' ')
    right_justify('em python')

""" Learning about conditionals
    Pay attention to the COLON after the condition
    Note else is different from elif
    """

import random


def guessing():
    count = 0
    draw = random.randint(0, 100)
    while True:
        guess = int(input('Entre um número inteiro entre 0 e 100: '))
        count += 1
        if guess > draw:
            print('Seu número está um pouco acima... Tente menor.')
        elif guess == draw:
            print('Parabéns!')
            print(f'Você acertou em {count} tentativas')
            return
        else:
            print('Tente um valor um pouco maior')


if __name__ == '__main__':
    guessing()

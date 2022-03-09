""" Curso Python IPEA - Flavio Carneiro
    Prof: Bernardo Furtado
    Exercício Slide 19 Aula 4
"""
import random


def med():
    counter = 1
    while True:
        guess = input('Digite um número inteiro entre 0 e 100: ')
        try:
            val = int(guess)
        except ValueError:
            print("Eu disse um número, criatura!")
            guess = input('Digite um número inteiro entre 0 e 100: ')
        if int(guess) == senha:
            print(f'Parabéns, você acertou em {counter} tentativas!')
            import turtle
            import trofeu
            trofeu.desenha_trofeu()
            turtle.mainloop()
            break
        elif int(guess) > senha:
            print('Muito grande!')
            counter += 1
        else:
            print('Muito pequeno!')
            counter += 1


def fac():
    counter = 1
    while True:
        guess = input('Digite um número inteiro entre 0 e 100: ')
        try:
            val = int(guess)
        except ValueError:
            print("Eu disse um número, criatura!")
            guess = input('Digite um número inteiro entre 0 e 100: ')
        if int(guess) == senha:
            print(f'Parabéns, você acertou em {counter} tentativas!')
            import turtle
            import trofeu
            trofeu.desenha_trofeu()
            turtle.mainloop()
            break
        elif int(guess) > senha:
            if int(guess) > senha + 30:
                print('Muuuuuuito grande!')
                counter += 1
            elif int(guess) > senha + 10:
                print('Muito grande!')
                counter += 1
            else:
                print('Grande, mas está perto!')
                counter += 1
        else:
            if int(guess) < senha - 30:
                print('Muuuuuuito pequeno!')
                counter += 1
            elif int(guess) < senha - 10:
                print('Muito pequeno!')
                counter += 1
            else:
                print('Pequeno, mas está perto!')
                counter += 1


def dif():
    tentativas = input('Digite o número máximo de tentativas (até 10): ')
    try:
        val = int(tentativas)
    except ValueError:
        print("Eu disse um número, criatura!")
        tentativas = input('Digite o número máximo de tentativas (até 10): ')
    if int(tentativas) > 10:
        tentativas = 10
        print('Número maior que 6, selecionado 10 tentativas')

    counter = 1
    while counter <= int(tentativas):
        guess = input('Digite um número inteiro entre 0 e 100: ')
        try:
            val = int(guess)
        except ValueError:
            print("Eu disse um número, criatura!")
            guess = input('Digite um número inteiro entre 0 e 100: ')
        if int(guess) == senha:
            print(f'Parabéns, você acertou em {counter} tentativas!')
            import turtle
            import trofeu
            trofeu.desenha_trofeu()
            turtle.mainloop()
            break
        elif int(guess) > senha:
            print(f'Muito grande! {int(tentativas) - counter} tentativa(s) restante(s)')
            counter += 1
        else:
            print(f'Muito pequeno! {int(tentativas) - counter} tentativa(s) restante(s)')
            counter += 1
    print('Game Over')


def select_level():
    level = input('Escolha o nível: fácil (f), médio (m) ou difícil (d): ')
    if level == 'f' or level == 'fácil':
        fac()
    elif level == 'm' or level == 'médio':
        med()
    elif level == 'd' or level == 'difícil':
        dif()
    else:
        select_level()


if __name__ == '__main__':
    senha = random.randint(0, 100)
    select_level()



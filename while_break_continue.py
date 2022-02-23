

def got_it(number):
    while number > 0:
        print(f'Going down... {number}')
        number -= 1


def while_true():
    while True:
        ipt = input('Do you wanna stop?')
        print(ipt)
        if ipt == 'YES!':
            break


def divisivel_por(n):
    for i in range(n):
        n -= 1
        if n % 13 == 0:
            print(f'{n} é divisível por 13')
        else:
            continue
            print('This is an never going to print')
        print(f'Chegamos até aqui, n é: {n}')


def outro_continue_ou_break(test):
    for letter in 'frase h grande':     # First Example
        if letter == 'h':
            if test == "break":
                break
            if test == "continue":
                continue
        print('Current Letter :', letter)
    print('Saímos do loop!')


if __name__ == '__main__':
    # got_it(100)
    # while_true()
    divisivel_por(100)
    # print('chamando break')
    # outro_continue_ou_break('break')
    # print('chamando continue')
    # outro_continue_ou_break("continue")

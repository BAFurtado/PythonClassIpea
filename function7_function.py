import function1


def do_twice(f):
    # O parâmetro de entrada é uma função
    print('Rodando 1a vez:')
    f()
    print(' ')
    print('Rodando 2a vez:')
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


if __name__ == '__main__':
    do_twice(function1.print_sentences)

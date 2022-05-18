import sys
import os


def print_soma(n1, n2):
    print(f'A soma é: {n1 + n2}')


if __name__ == '__main__':

    if len(sys.argv) > 0:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print(os.system(sys.argv[3]))
    else:
        num1 = 1190
        num2 = 226
    print_soma(num1, num2)


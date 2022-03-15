""" From Think Python Allen Dowley """
import time


def countdown(n):
    if n <= 0:
        print('Blastoff! or  Lift off')
    else:
        print(n)
        time.sleep(.5)
        return countdown(n-1)


if __name__ == '__main__':
    m = 20
    countdown(m)

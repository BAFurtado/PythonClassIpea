""" Demonstrating how to reverse a string list by hand
    Try using the list method l.reverse()
"""


def reversing(name):
    b = list()
    for i in name:
        b.append(i)

    print(b)

    c = list()
    for i in range(len(b)):
        c.append(b.pop())

    print(c)
    print(''.join(c))


if __name__ == '__main__':
    ipt = 'Urso Grande'
    reversing(ipt)

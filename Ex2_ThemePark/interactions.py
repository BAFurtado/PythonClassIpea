import random

from Ex2_ThemePark.account import Agent, Shop
from Ex2_ThemePark import parameters


def creation(f, i, n, p):
    l = list()
    for i in range(i, n):
        l.append(f(i, p))
    return l


def interact(a, s):
    for i in range(len(a)):
        s1 = random.choice(s)
        if a[i].check_funds(s1):
            if s1.visit():
                s1.account.deposit(a[i].account.pay(s1.cost))
                a[i].get_fun(s1.fun)


def salaries(a, p):
    for i in range(len(a)):
        a[i].account.deposit(random.randrange(p['salaries'][0], p['salaries'][1]))


def averaging(a, s):
    avg_fun = sum([i.fun for i in a]) / len(a)
    # list comprehension
    avg_shop_balance = sum([i.account.balance for i in s]) / len(s)
    avg_consumer_balance = sum([i.account.balance for i in a]) / (len(a))
    # print(f'Average fun for this configuration is {avg_fun:.2f}')
    # print(f'Average shop balance for this configuration is {avg_shop_balance:.2f}')
    # print(f'Average consumer balance for this configuration is {avg_consumer_balance:.2f}')
    # print("")
    # print("----------------------------------")
    return avg_fun, avg_shop_balance, avg_consumer_balance


def main(n1, n2, p):
    agents = creation(Agent, 0, n1, None)
    shops = creation(Shop, n1, n1 + n2, p)
    random.shuffle(agents)
    random.shuffle(shops)
    salaries(agents, p)
    interact(agents, shops)

    return averaging(agents, shops)


if __name__ == '__main__':
    a = 500
    s = 200
    f, sb, cb = main(a, s, parameters.params)
    print(f'Average fun {f:.2f}')
    print(f'Average shop balance {sb:.2f}')
    print(f'Average consumer balance {cb:.2f}')

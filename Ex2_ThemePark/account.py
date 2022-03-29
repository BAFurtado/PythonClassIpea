import random
from Ex2_ThemePark.parameters import params as par


class Account:
    def __init__(self, i):
        self.balance = 0
        self.registration = i

    def deposit(self, amount):
        self.balance += amount
        # print('Your current balance is {}'.format(self.balance))

    def check_funds(self, amount):
        if self.balance - amount < 0:
            return False
        else:
            return True

    def pay(self, amount):
        self.balance -= amount
        return amount


class Shop:
    def __init__(self, i, p):
        self.account = Account(i)
        self.capacity = random.randrange(p['capacity'][0], p['capacity'][1])
        self.fun = random.randrange(p['fun'][0], p['fun'][1])
        self.cost = random.randrange(p['cost'][0], p['cost'][1])
        # print(f'Shop {i} created')

    def check_capacity(self):
        if self.capacity <= 0:
            return False
        else:
            return True

    def visit(self):
        if self.check_capacity() > 0:
            self.capacity -= 1
            # print('A visit has been completed')
            return True
        else:
            return False


class Agent:
    def __init__(self, *args):
        self.account = Account(args[0])
        self.fun = 0
        # print(f'Agent {i} created')

    def get_fun(self, amount):
        self.fun += amount
        # print(f'Agent has {self.fun} fun right now')

    def check_funds(self, shop):
        if self.account.balance > shop.cost:
            return True
        else:
            return False


if __name__ == '__main__':
    # Tests
    # Creation
    # print(type(par))
    # print(par.keys())
    # print(par.values())
    # print(par)
    s1 = Shop(0, par)
    a1 = Agent(1, par)

    # a1 gets salary
    a1.account.deposit(100)
    #
    # #
    # # Interaction1
    # # a1 goes shopping at s1
    #
    # # a1 pays established price and s1 receives payment
    a1.account.pay(s1.cost)
    s1.account.deposit(10)
    s1.account.deposit(a1.account.pay(s1.cost))
    #
    # # visit
    print(s1.check_capacity())
    # s1.visit()
    # a1.get_fun(s1.fun)
    #
    # # funds
    # a1.check_funds(s1)
    
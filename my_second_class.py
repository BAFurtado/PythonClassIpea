from my_first_class import Animal


class Dog(Animal):

    def sound(self):
        return 'bark, bark, bark'


class Cat(Animal):

    def sound(self):
        return 'miaouw, miaouw, miaouw'


if __name__ == '__main__':
    a = Dog('Carmela')
    print(a.age)
    print(a.name)
    print(a)
    print(a.sound())
    b = Cat('James')
    print(b.sound())
    print(f'{b.name} is {b.age} years old')
    b.get_old()
    print(f'{b.name} is {b.age} years old')

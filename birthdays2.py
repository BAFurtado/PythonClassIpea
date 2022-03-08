import random


def create_birthdays(students: int) -> list:
    # Use random.randint to create a list of birthdays
    pass


def duplicados(birthdays: list) -> bool:
    # Verifique se a lista tem duplicados
    # Lembre-se a função set() retorna um objeto sem duplicados

    # Brincadeira abaixo:
    return random.choice([False, True])


def simulations(number: int) -> str:
    # Chame a função create_birthdays e duplicados repetidmaente (number) e calcule a probabilidade
    pass


if __name__ == '__main__':
    n_simulation = 10
    n_students = 50

    # Teste para duplicados
    a = [1, 100, 101]  # False
    b = [1, 100, 1]  # True
    assert duplicados(a) is False
    assert duplicados(b) is True

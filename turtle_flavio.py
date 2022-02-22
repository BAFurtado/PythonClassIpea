# Exercício

import turtle
import math


# Função que constrói polígono de n lados e tamanho length, com a tartaruga t:
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# Função que desenha um círculo aproximado de raio r usando a tartaruga t
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


def main():
    # Definindo Tartarugas Desenhadoras
    joao = turtle.Turtle()
    maria = turtle.Turtle()

    # Preparando posições e cores
    joao.color("red")
    joao.speed(3)
    maria.color("blue")
    maria.rt(4 * 180 / 5)
    maria.speed(3)

    # Desenhando
    for i in range(4):
        circle(joao, 100)
        polygon(maria, 5, 100)
        joao.rt(90)
        maria.rt(90)
    joao.pu()
    joao.rt(90)
    joao.fd(200)
    joao.rt(270)
    joao.pd()
    joao.pensize(3)
    circle(joao, 200)

    turtle.mainloop()


if __name__ == '__main__':
    main()


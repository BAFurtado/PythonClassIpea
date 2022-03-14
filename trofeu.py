# Exercício

import turtle
import math


def arc(turt, radius, angle):
    circumference = 2 * radius * math.pi
    leng = circumference / 360
    turt.speed(100000)
    for s in range(angle):
        turt.fd(leng)
        turt.rt(1)
    turt.speed(2)


# Definindo Tartarugas Desenhadoras
def desenha_trofeu():
    t = turtle.Turtle()
    t.color("gold3")
    t.penup()
    t.fd(10)
    t.pendown()
    t.fd(40)
    t.rt(90)
    t.fd(90)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(90)
    t.rt(90)
    t.fd(40)
    t.rt(270)
    t.fd(100)
    t.rt(270)
    arc(t, 90, 90)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    arc(t, 90, 90)
    t.rt(270)
    t.fd(98)
    t.hideturtle()


if __name__ == '__main__':
    desenha_trofeu()
    turtle.mainloop()

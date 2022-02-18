import turtle
import random


def polygon(n, t, c):
    # n é o número de lados do poligono
    # t é o tamanho em passos do objeto
    b = turtle.Turtle()
    b.color(c)
    b.speed(2)
    b.penup()
    b.forward(random.randint(-100, 100))
    b.pendown()
    for i in range(n):
        b.forward(t)
        b.lt(360/n)


if __name__ == '__main__':
    for col in ['red', 'blue', 'green', 'orange', 'purple']:
        polygon(7, 95, col)
    turtle.mainloop()

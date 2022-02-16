"""
Adapted from Think Python 2, by Allen Downey. Chapter 4
"""

import turtle


def square(agent, l):
    """ Receives a turtle and moves it in a square

    """
    agent.speed(2)
    for i in range(4):
        agent.fd(l)
        agent.lt(90)


def make_polygon(agent, l, n):
    angle = 360 / n
    for i in range(n):
        agent.fd(l)
        agent.lt(angle)


if __name__ == '__main__':
    maria = turtle.Turtle()
    print(id(maria))
    jose = turtle.Turtle()
    maria.color('red')
    # Check that now the turtle is an argument
    square(maria, 100)
    # square is the function we created
    square(jose, 75)
    # Here the turtle is an object that uses a method
    jose.penup()
    jose.setpos(-100, -100)
    jose.pendown()
    square(jose, -75)
    jose.color('green')
    jose.pensize(4)
    make_polygon(jose, 100, 6)
    maria.color('blue')
    maria.pensize(2)
    make_polygon(maria, 10, 36)
    turtle.mainloop()

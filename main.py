import random

from turtle import Turtle, Screen, bgcolor, colormode

t = Turtle()
colormode(255)

t.speed("fastest")
bgcolor("black")


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


t_continue = True
while t_continue:
    t.color(color())
    t.circle(100)
    current_heading = t.heading()
    t.setheading(current_heading + 3)
    if current_heading == 357:
        t_continue = False

screen = Screen()
screen.exitonclick()

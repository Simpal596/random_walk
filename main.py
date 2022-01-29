
from turtle import Turtle, Screen, colormode
from random import randint


timmy = Turtle()
timmy.shape("turtle")
colormode(255)
timmy.speed(0)



def random_color() :
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tuple = (r,g,b)
    return tuple


for i in range(0,360,5) :
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(i)
    print(i)



my_screen = Screen()

my_screen.exitonclick()

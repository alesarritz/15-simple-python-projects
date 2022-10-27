from turtle import Turtle, Screen
from random import randint, choice
import colorgram
TURTLE_SIZE = 20
colors = colorgram.extract('image.jpg', 10)

tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.speed("fastest")
tim.hideturtle()
tim.penup()

initial_x = - screen.window_width()/3.5
tim.goto(initial_x, screen.window_height()/3)

for i in range(10):
    for _ in range(10):
        tim.dot(20, choice(colors).rgb)
        tim.forward(50)
    tim.goto(initial_x, tim.ycor() - 50)






screen.exitonclick()

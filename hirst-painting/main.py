from turtle import Turtle, Screen, colormode
import random

colors = [(1, 12, 31), (54, 25, 17), (218, 127, 106), (9, 104, 160), (242, 213, 68), (150, 83, 39), (216, 86, 63), (156, 6, 24), (165, 162, 30), (158, 62, 102), (207, 73, 103), (10, 64, 33), (11, 96, 57), (95, 6, 20), (175, 134, 162), (7, 173, 217), (1, 61, 145), (2, 213, 207), (158, 32, 23), (8, 140, 85), (144, 227, 217), (121, 193, 147), (220, 177, 216), (100, 218, 229), (251, 198, 1), (116, 170, 192), (79, 134, 178), (28, 84, 93), (228, 174, 165), (186, 190, 201), (72, 77, 35)]

colormode(255)

tim = Turtle()
screen = Screen()

tim.speed(0)

def draw_circle():
    tim.color(random.choice(colors))
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()

def set_position(x ,y):
    tim.penup()
    tim.setposition(x, y)
    tim.pendown()

for row in range(10):
    position_x = -250
    position_y = -250 + row * 40
    set_position(position_x, position_y)
    for column in range(10):
        draw_circle()
        tim.penup()
        tim.forward(50)


screen.exitonclick()


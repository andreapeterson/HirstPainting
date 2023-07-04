# import colorgram
#
#
# colors = colorgram.extract('hirst.jpg', 100)
# color_palette = []
# for color in range(len(colors)):
#     r = colors[color].rgb.r
#     g = colors[color].rgb.g
#     b = colors[color].rgb.b
#     new_color = (r, g, b)
#     color_palette.append(new_color)
# print(color_palette)


import random
import turtle as t


turtle = t.Turtle()
turtle.shape("circle")
turtle.speed("fastest")
turtle.pensize(20)
t.colormode(255)


# Below is the updated color list without whites
color_palette2 = [(220, 153, 106), (131, 171, 196), (221, 72, 87), (216, 131, 149), (23, 119, 153),
                  (242, 208, 98), (120, 177, 148), (37, 118, 81), (20, 164, 205), (141, 86, 62), (222, 82, 76),
                  (126, 86, 105), (173, 184, 216), (20, 166, 121), (163, 209, 167), (3, 97, 116), (175, 155, 75),
                  (55, 60, 94), (236, 162, 175), (239, 169, 155), (145, 207, 223), (85, 126, 182), (24, 99, 84),
                  (48, 64, 76)]


def new_row():
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(180)


def starting_position():
    turtle.setheading(220)
    turtle.penup()
    turtle.forward(320)
    turtle.setheading(0)


starting_position()
for x in range(10):
    for y in range(10):
        turtle.pencolor(random.choice(color_palette2))
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)
    new_row()


turtle.hideturtle()


screen = t.Screen()
screen.exitonclick()

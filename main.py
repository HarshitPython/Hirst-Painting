import colorgram

rgb_colours = []

colors = colorgram.extract('Image.jpg',30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_colors = (r, g, b)
    rgb_colours.append(new_colors)

print(rgb_colours)

from turtle import Turtle,Screen
import random
import turtle
turtle.colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list=[(229, 222, 215), (231, 220, 224), (218, 229, 219), (215, 225, 233),
            (227, 206, 101), (210, 161, 104), (126, 167, 183), (156, 14, 22), 
            (43, 107, 150), (129, 171, 142), (188, 71, 36), (223, 84, 58), 
            (9, 38, 76),(198, 186, 34),(12, 59, 36), (165, 19, 14), (35, 130, 52), 
            (13, 92, 45), (96, 9, 16),(63, 20, 17), (144, 73, 80), (59, 163, 82),
            (175, 136, 146),(11, 62, 131), (238, 201, 7),(204, 72, 78), (58, 148, 185), 
            (235, 170, 162), (79, 132, 181), (171, 205, 178)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
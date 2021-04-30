from turtle import Turtle, Screen
import random

t = Turtle()

t.shape("turtle")

t.color("blue")

angle = 72

start = 1


# def trianle():
#     t.right(60)
#     t.forward(60)
#     t.right(120)
#     t.forward(60)
#     t.right(120)
#     t.forward(60)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for item in range(3,11):
    t.color(random.choice(colours))
    draw_shape(item)

# show the screen and when it is clicked screen dissapears
screen = Screen()
screen.exitonclick()

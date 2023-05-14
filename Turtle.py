# Turtle 
import turtle
import math

screen = turtle.Screen()
laki = turtle.Turtle()
laki.color("green","pink")
laki.shape("turtle")

laki.speed(100)
laki.begin_fill()

for i in range(2000):
    laki.forward(10)
    laki.left(math.sin(i/10)*25)
    laki.left(20)

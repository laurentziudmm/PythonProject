#Creating a simple color wheel in Python
#first, import graphics capabilities
from turtle import *
#create a window for the graphics
from setuptools import setup

setup()
#create a turtle for drawing
t1 = Turtle()

#create a list of colors to randomly choose from
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

#import random capabilities
import random

#do some basic setup for the turtle
#pick up the pen so no marks are left
t1.up()
#move the turtle to the left
t1.goto(-200,0)
#put the pen back down
t1.down()
#change the pen thickness
t1.width(5)
#hide the turtle icon
t1.hideturtle()
#set turtle speed to MAXIMUM (1-10 for specific speeds. 1 is slowest)
t1.speed(0)

#create a loop for the graphics to be built
for i in range(9001):
    #choose a random color for the turtle
    colorchoice = random.choice(colors)
    #have the turtle take on the randomly chose color
    t1.color(colorchoice)
    #move the turtle forward
    t1.forward(400)
    #have the turtle turn 181 degrees (anything over 180 works)
    t1.right(181)
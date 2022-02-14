import time

import graphics
from graphics import *

width = 500
height = 500
win = GraphWin("Clicks", width, height)

#Shape Variables

Heart_Circle_Left = Circle(Point(200,150),75)
Heart_Circle_Right = Circle(Point(300,150),75)
Square_Heart = Polygon(Point(145,200),Point(356,200),Point(250,350))
Background = Rectangle(Point(0,0),Point(width,height))

Background.setFill("black")
Heart_Circle_Left.setFill("red")
Heart_Circle_Right.setFill("red")
Square_Heart.setFill("red")

#Text Variables
val_text = Text(Point(250,450),"Happy Valentines day")

#sets colors and outline

Background.setOutline("black")
Heart_Circle_Left.setOutline("red")
Heart_Circle_Right.setOutline("red")
Square_Heart.setOutline("red")

val_text.setFill("red")
val_text.setSize(20)

#moves arrow and blood

def Valentines():
    time.sleep(0.5)
    val_text.draw(win)
    time.sleep(0.5)

    Arrow = Polygon(Point(500,225),Point(725,215),Point(725,235))
    Arrow.setFill("white")
    Arrow.draw(win)

    Heart_Puncture = Rectangle(Point(300,200),Point(200,250))
    Heart_Puncture.setFill("red")
    Heart_Puncture.setOutline("red")
    Heart_Puncture.draw(win)

    Blood_1 = Circle(Point(300,200),5)
    Blood_1.setFill("red")
    Blood_1.setOutline("red")
    Blood_1.draw(win)

    Blood_2 = Circle(Point(250, 200), 7)
    Blood_2.setFill("red")
    Blood_2.setOutline("red")
    Blood_2.draw(win)

    for i in range(38):
        Arrow.move(-10,0)
        time.sleep(0.01)

    for j in range(100):
        Blood_1.move(0,3)
        Blood_2.move(0,5)
        time.sleep(0.01)

#draws the heart and background

Background.draw(win)
Heart_Circle_Left.draw(win)
Heart_Circle_Right.draw(win)
Square_Heart.draw(win)


Valentines()


input()
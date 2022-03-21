import time
from graphics import *
from random import randint
from math import sqrt


def get_random(R1, R2):
    return randint(R1,R2)

def did_collide(Circle_1, Circle_2): #Checks to see if circles collided
    radius_1 = Circle_1.getRadius()
    radius_2 = Circle_2.getRadius()

    c1_x = Circle_1.getCenter().getX()
    c1_y = Circle_1.getCenter().getY()

    c2_x = Circle_2.getCenter().getX()
    c2_y = Circle_2.getCenter().getY()

    circle_distance = sqrt(
        (c2_x - c1_x) ** 2 + (c2_y - c1_y) ** 2)
    if circle_distance < radius_1 + radius_2:
        return True

def hit_vertical(Circle, win): #Checks to see if a circle hit a wall
    if Circle.getCenter().getX() >= win.height - 40:
        return True
    elif Circle.getCenter().getX() <= 40:
        return True
    else:
        return False

def hit_horizontal(Circle, win): #Checks to see if a circle hit the floor or ceiling
    if Circle.getCenter().getY() >= win.width - 40:
        return True
    elif Circle.getCenter().getY() <= 40:
        return True
    else:
        return False

def random_color():
    R = randint(0,255)
    G = randint(0, 255)
    B = randint(0, 255)
    color = color_rgb(R,G,B)
    return color

def bumper():
    height = 500
    width = 500
    win = GraphWin('Bumper',height,width)

    circle_1 = Circle(Point(250,200),40)
    circle_1.setFill(random_color())

    circle_2 = Circle(Point(250, 300),40)
    circle_2.setFill(random_color())

    circle_1.draw(win)
    circle_2.draw(win)

    index = 0
    c1_dir_x = get_random(-5,5)
    c1_dir_y = get_random(-5,5)

    c2_dir_x = get_random(-5, 5)
    c2_dir_y = get_random(-5, 5)
    while index != 1:
        circle_1.move(c1_dir_x,c1_dir_y)
        circle_2.move(c2_dir_x,c2_dir_y)
        if hit_horizontal(circle_1, win):
            c1_dir_y = c1_dir_y * -1
        elif hit_vertical(circle_1,win):
            c1_dir_x = c1_dir_x * -1

        if hit_horizontal(circle_2, win):
            c2_dir_y = c2_dir_y * -1
        elif hit_vertical(circle_2,win):
            c2_dir_x = c2_dir_x * -1

        if did_collide(circle_1,circle_2):
            c1_dir_y = c1_dir_y * -1
            c1_dir_x = c1_dir_x * -1
            c2_dir_y = c2_dir_y * -1
            c2_dir_x = c2_dir_x * -1
            circle_1.setFill(random_color())
            circle_2.setFill(random_color())


        time.sleep(0.0001)

    win.getMouse()

bumper()
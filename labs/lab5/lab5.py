import math

import graphics
from graphics import *

height = 500
width = 500

def triange():



    win = GraphWin("Triangle",height,width)

    click_1 = win.getMouse()
    first_point = Point(click_1.getX(), click_1.getY())
    first_point.draw(win)

    click_2 = win.getMouse()
    second_point = Point(click_2.getX(), click_2.getY())
    second_point.draw(win)

    click_3 = win.getMouse()
    third_point = Point(click_3.getX(), click_3.getY())
    third_point.draw(win)

    tri_shape = Polygon(first_point,second_point,third_point)
    tri_shape.setFill("red")
    tri_shape.draw(win)

    line_len_X1 = click_1.getX() - click_2.getX()
    line_len_Y1 = click_1.getY() - click_2.getY()

    line_len_X2 = click_2.getX() - click_3.getX()
    line_len_Y2 = click_2.getY() - click_3.getY()

    line_len_X3 = click_3.getX() - click_1.getX()
    line_len_Y3 = click_3.getY() - click_1.getY()

    a = math.sqrt((line_len_X1) ** 2 + (line_len_Y1) ** 2)
    b = math.sqrt((line_len_X2) ** 2 + (line_len_Y2) ** 2)
    c = math.sqrt((line_len_X3) ** 2 + (line_len_Y3) ** 2)

    distance = a + b + c

    s = (a + b + c)/2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))


    perm_text = Text(Point(height/2,width/1.1),"Perimeter: " + str(distance))
    perm_text.draw(win)

    area_text = Text(Point(height / 2, width / 1.25), "Area: " + str(area))
    area_text.draw(win)

    print(distance)
    print(area)

    win.getMouse()
triange()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text_entry_pt = Point(win_width / 2, win_height / 2 + 40)
    red_entry = Entry(red_text_entry_pt, 5)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_entry_pt = red_text_entry_pt.clone()
    green_text_entry_pt.move(0,30)
    green_entry = Entry(green_text_entry_pt, 5)
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()

    blue_text_entry_pt = red_text_entry_pt.clone()
    blue_text_entry_pt.move(0, 60)
    blue_entry = Entry(blue_text_entry_pt, 5)
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    close_text = Text(Point(height / 2, width / 1.5), "Click to close")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_entry.draw(win)
    green_entry.draw(win)
    blue_entry.draw(win)

    for i in range(5):
        win.getMouse()
        r= int(red_entry.getText())
        b = int(blue_entry.getText())
        g = int(green_entry.getText())


        shape.setFill(color_rgb(r,g,b))
        print(i)

    close_text.draw(win)


    # Wait for another click to exit
    win.getMouse()
    win.close()

color_shape()

def process_string():
    text = input("Enter a string\n")

    print(text[0])
    print(text[len(text)-1])
    print(text[2:5])
    print(text[0] + text[len(text)-1])
    for i in range(10):
        print(text[0:3])
    for r in range(len(text)):
        print(text[r])
    print("There are",len(text),"characters in this string")

process_string()

def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2],values[3],values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print("There are",x,"things in the list")


process_list()

def another_series():
    value = eval(input("How many numbers in the series:\n"))
    result = 0
    for i in range(value):
        a = (((i % 3)+1)*2)
        print(a, end="+")
        result = result + a
    print()
    print("Result:",result)

another_series()

def target():
    win = GraphWin("Target", height, width)

    center_pt = Point(height/2,width/2)
    circ_size = 2
    tar_cir = Circle(center_pt,height / circ_size)
   # tar_cir.draw(win)
    color_list = ["red","black"]
    index = 1


    for i in range(9):
        tar_cir.draw(win)
        circ_size = circ_size + i
        tar_cir = Circle(center_pt, height / circ_size)

        index = i % 2

        tar_cir.setFill(color_list[index])


    win.getMouse()
target()

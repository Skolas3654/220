"""
Name: Andreas Dilling
hw4.py

Problem: <Brief, one or two sentence description of
the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math

from graphics import *

width = 400
height = 400

def squares():
    # Creates a graphical window
    win = GraphWin("Clicks", width, height)

    # number of times user can move square
    num_clicks = 6

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)



    # allows the user to click multiple times to move the square
    for i in range(num_clicks):

        click = win.getMouse()

        shape = Rectangle(Point(click.getX()-25, click.getY()-25), Point(click.getX()+25, click.getY()+25))
        shape.setOutline("red")
        shape.setFill("red")
        shape.ge

        shape.draw(win)

    instructions_pt = Point(width / 2, height - 100)
    instructions = Text(instructions_pt, "Looking good, Click again to close")
    instructions.draw(win)

    win.getMouse()
    win.close()

#squares()

def rectangle():
    win = GraphWin("Rectangle",height,width)

    inst_pt = Point(width / 2, height - 25)
    instructions = Text(inst_pt, "Click two points on screen")
    instructions.draw(win)

    click_1 = win.getMouse()
    first_point = Point(click_1.getX(),click_1.getY())
    first_point.draw(win)

    click_2 = win.getMouse()
    second_point = Point(click_2.getX(), click_2.getY())
    second_point.draw(win)

    rect = Rectangle(first_point, second_point)
    rect.setFill("Green")
    rect.setOutline("Black")
    rect.draw(win)
    print(first_point)
    print(second_point)

    instructions.setText("Wonderful! Now click again to close")


    rec_len = abs(first_point.getX()) - abs(second_point.getX())
    rec_wid = abs(first_point.getY()) - abs(second_point.getY())

    area = abs(rec_len * rec_wid)
    perim = abs(2 * (rec_len+rec_wid))

    area_pt = Point(width / 2, height - 80)
    area_display = Text(area_pt, "Area: "+ str(area))
    area_display.draw(win)



    perim_pt = Point(width / 2, height - 100)
    perim_display = Text(perim_pt, "Perimeter: "+ str(perim))
    perim_display.draw(win)

    print(rec_len)
    print(rec_wid)


    win.getMouse()


#rectangle()



def circle():
    win = GraphWin("Circle", height, width)

    center_point = win.getMouse()
    circ_center = Point(center_point.getX(), center_point.getY())
    circ_center.draw(win)

    outer_point = win.getMouse()
    circ_outer = Point(outer_point.getX(), outer_point.getY())
    circ_outer.draw(win)

    par_1 = (outer_point.getX() - center_point.getX()) ** 2
    par_2 = (outer_point.getY() - center_point.getY()) ** 2
    radius = round(math.sqrt(par_1 + par_2),3)

    cir = Circle(center_point, radius)
    cir.setFill("Dark Blue")
    cir.setOutline("Yellow")
    cir.draw(win)

    radius_pt = Point(width / 2, height - 100)
    radius_text = Text(radius_pt,"Radius: " + str(radius))
    radius_text.draw(win)

    instructions_pt = Point(width / 2, height - 25)
    instruction_text = Text(instructions_pt, "Nice Job, Click to close, or don't, I'm not your dad")
    instruction_text.draw(win)

    win.getMouse()

#circle()

def pi2():
    value_amount = eval(input("Enter the number of terms to sum:\n"))
    approx = 0

    for i in range(1,value_amount * 2,2):
        #Calculates the denominator
        approx = -1 * (approx + (4/i))


    approx = abs(approx)
    print(approx)

    accuracy = math.pi - approx
    print("Accuracy:", abs(accuracy))

#pi2()

if __name__ == '__main__':
    pass

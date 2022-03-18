"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the
 problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math

from graphics import GraphWin, Circle, Text, Point

def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10

def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def sum_list(nums):
    res = 0
    for i in range(len(nums)):
        res = nums[i] + res
    return res

def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])

def sum_of_squares(nums):
    res_list = []
    for i in range(len(nums)):
        nums.append(nums[i])
        for r in range(len(nums)):
            res = 0
            element = nums[r]
            element = element.replace(",","").split()
            for s in range(len(element)):
                element[s] = float(element[s])
                res = res + element[s]**2
        res_list.append(res)
    return res_list



def starter(weight, wins):
    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    elif weight >= 200 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0) or (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius_2 = math.sqrt(
        (center_2.getX() - circumference_point_2.getX()) ** 2 + (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill("red")
    circle_two.draw(win)


#circle_overlap()

def did_overlap(circle_one, circle_two):

    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt((center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius_2 = math.sqrt((center_2.getX() - circumference_point_2.getX()) ** 2 + (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill("red")
    circle_two.draw(win)

    answer_text = Text(Point(4, 3), "")
    close_text = Text(Point(4, 2.5), "Click again to close")

    circle_distance = math.sqrt((center_2.getX() - center.getX()) ** 2 + (center_2.getY() - center.getY()) ** 2)
    if circle_distance < radius + radius_2:

        answer_text.setText("The circles overlap.")
        answer_text.draw(win)
        close_text.draw(win)
        win.getMouse()

        return True

    else:
        answer_text.setText("The circles do not overlap")
        answer_text.draw(win)
        close_text.draw(win)
        win.getMouse()

        return False


if __name__ == '__main__':
    pass

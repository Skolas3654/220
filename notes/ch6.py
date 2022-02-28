import math
import time

import graphics
from graphics import *

def birthday(message):
    print(message)

def sing(name, holiday, tod):
    print("hey {}, have a good {} and {}".format(name,holiday,tod))


def square(num):
    squared = num * num
    return squared

def distance(p1,p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2-y1, 2))
    return d

d = distance(Point(2,3), Point(150,200))
#print(d)

def cool():
    height = 500
    width = 500

    win = GraphWin("Target", height, width)

    center_pt = Point(height / 2, width / 2)
    circ_size = 2
    tar_cir = Circle(center_pt, height / circ_size)
    # tar_cir.draw(win)

    for i in range(500):
        tar_cir.draw(win)
        circ_size = circ_size - 0.5
        tar_cir = Circle(center_pt, i)

    input()


def diff(x,y):
    sum_value = x + y
    diff_val = x - y
    return sum_value, diff_val

#s,r = diff(5,10)
#print(s)
#print(r)

def sale_price(price, sale):
    amount = price * (1-sale)
    return amount

#sales_amount = sale_price(100,0.2)
#print(sales_amount)

def double_list(list_one):
    for i in range(len(list_one)):
        list_one[i] = list_one[i] * 2
    return  list_one


my_list = [1,2,3,4,5]
my_other_list = my_list

double_list(my_list)
print(my_list, my_other_list)

def double_value(value_one):
    value_one = value_one * 2
    return value_one

value = 7
print(value)
double_value(value)
print(value)

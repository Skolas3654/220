from graphics import *

def read_data(filename):
    file = open(filename, 'r')
    text = file.read()
    text = text.replace("\n"," ")
    str_list = text.split()
    return str_list

def is_in_linear(search_val, values):
    index = 0
    length = len(values)-1
    while (int(values[index]) != search_val) and (index < length):
        index += 1
        if int(values[index]) == search_val:
            return True
    return False

def is_in_binary(search_val,values):
    low = 0
    high = len(values) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if values[mid] < search_val:
            low = mid + 1
        elif values[mid] > search_val:
            high = mid - 1
        else:
            return True
    return False

def selection_sort(values):
    n = len(values)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if (values[j] < values[minimum]):
                minimum = j
        temp = values[i]
        values[i] = values[minimum]
        values[minimum] = temp
def calc_area(rect):
    p1x = rect.getP1().getX()
    p2x = rect.getP2().getX()
    p1y = rect.getP1().getY()
    p2y = rect.getP2().getY()

    l = abs(p2x - p1x)
    w = abs(p2y - p1y)
    return(l*w)

def rect_sort(rectangles):
    rectangles.sort(key=calc_area)

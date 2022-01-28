"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes():
    upper_bond = eval(input("What is the upper bond: \n"))
    for i in range(0, upper_bond + 1, 3):
        print(i)
    result = upper_bond * 3
    print("Sum of threes is", result)



def multiplication_table():
    index = 1
    min_row = 1
    max_row = 11
    for i in range(1,11):
        for y in range(min_row,max_row,index):

            print(y, end=" ")
        print("\n")
        index = index + 1
        max_row = max_row + 10
        min_row = min_row + 1



def triangle_area():
    a = eval(input("What length is side a:\n"))
    b = eval(input("What length is side b:\n"))
    c = eval(input("What length is side c:\n"))
    area = (a+b+c)/2
    print("The area is",area)



def sum_squares():
    lower_range = eval(input("Enter the lower range:\n"))
    upper_range = eval(input("Enter the upper range:\n"))
    sum = 0
    for i in range(lower_range,upper_range+1):
        sum = sum + i * i
    print("Your result is",sum)






def power():
    base = eval(input("Enter base: \n"))
    static_base = base
    exponent = eval(input("Enter exponent: \n"))
    for i in range(exponent-1):
        base = (base * static_base)
    print(static_base,"^",exponent,"=",base)



if __name__ == '__main__':
    pass

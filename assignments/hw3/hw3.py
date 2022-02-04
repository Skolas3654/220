"""
Name: Andreas Dilling
hw3.py

Problem:

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""



def average():
    avrg_grade = 0
    value_amount = eval(input("How many grades will you enter: \n"))
    for i in range(value_amount):
        grade = eval(input("Enter grade:\n"))
        avrg_grade = avrg_grade + grade
    avrg_grade = avrg_grade/value_amount
    print(avrg_grade)

def tip_jar():
    total_amount = 0
    for i in range(5):
        tip = eval(input("How much would you like to donate?\n"))
        total_amount = total_amount + tip
    print("Total amount is", total_amount)


def newton():
    value = eval(input("What number do you want to square root?\n"))
    attempts = eval(input("How many times should we improve the approximation?\n"))
    approx = value
    for i in range(attempts):
        approx = ((approx+(value/approx))/2)
    print("The square root is approximately",approx)



def sequence():
    term_amount = eval(input("How many terms would you like?\n"))

    for i in range(term_amount):
        print(1+2*(i//2),end=" ")




def pi():
    acc = 1
    num = 2
    term_value = eval(input("How many product terms\n"))

    for i in range(term_value):
        index_1 = num/(num -1)
        index_2 = num/(num + 1)

        acc = acc * index_1 * index_2

        num = num + 2


    pi_result = acc * 2
    print(pi_result)



if __name__ == '__main__':
    pass

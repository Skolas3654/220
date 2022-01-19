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


def calc_rec_area():
    width = eval(input("Enter the width:"))
    length = eval(input("Enter the length:"))
    area = width*length
    print("The area of the rectangle is:", area)


def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length*width*height
    print("The volume is", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    player_shots = eval(input("Enter the shots the player made:"))
    shot_percent = (player_shots/total_shots)*100
    print("Your total is:",shot_percent, "%")


def coffee():
    coffee_pounds = eval(input("How many pounds of coffee would you like? "))
    total = coffee_pounds*(10.50+0.86) + 1.5
    print("Your total is $", total)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    miles = kilometers/1.61
    print("You traveled", miles, "miles")


if __name__ == '__main__':
    pass

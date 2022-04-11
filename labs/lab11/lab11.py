from lab10.door import Door
from lab10.button import Button
from graphics import GraphWin, Point, Rectangle, Text
from random import randint

def set_secretdoor(door1,door2,door3):
    secret_door = randint(0, 2)
    if secret_door == 0:
        door1.set_secret(True)
        door2.set_secret(False)
        door3.set_secret(False)
    if secret_door == 1:
        door1.set_secret(False)
        door2.set_secret(True)
        door3.set_secret(False)
    if secret_door == 2:
        door1.set_secret(False)
        door2.set_secret(False)
        door3.set_secret(True)

def show_secret_door(door_1,door_2,door_3):
    if door_1.is_secret():
        door_1.color_door('green')
    elif door_1.is_secret():
        door_2.color_door('green')
    else:
        door_3.color_door('green')
def reset(door_1,door_2,door_3,try_again_text, info_text):
    door_1.color_door('brown')
    door_2.color_door('brown')
    door_3.color_door('brown')
    try_again_text.setText("")
    info_text.setText('Click to guess which is secret door')

def result(result, door, info_text, try_again_text, win):
    try_again_text.setText("Click to play again")
    if result:
        door.color_door('green')
        info_text.setText("Congrats, you guessed correctly!")
    else:
        door.color_door('red')
        info_text.setText("You chose the wrong door")
    win.getMouse()


def main():
    wins = 0
    losses = 0

    win = GraphWin("Door Game", 500,500)

    quit_button = Button(Rectangle(Point(345,25),Point(445,75)),"Exit")
    win_button = Button(Rectangle(Point(25,100),Point(125,50)),wins)
    loss_button = Button(Rectangle(Point(125,100),Point(225,50)),losses)

    win_text = Text(Point(75,25),'wins')
    loss_text = Text(Point(175,25),'losses')

    info_text = Text(Point(250,175),'Click to guess which is secret door')
    try_again_text = Text(Point(250, 475), '')

    door_1 = Door(Rectangle(Point(50,200),Point(170,450)),"Door 1")
    door_2 = Door(Rectangle(Point(190,200),Point(310,450)),"Door 2")
    door_3 = Door(Rectangle(Point(330,200),Point(450,450)),"Door 3")




    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)
    win_button.draw(win)
    loss_button.draw(win)

    win_text.draw(win)
    loss_text.draw(win)

    info_text.draw(win)
    try_again_text.draw(win)

    quit_button.draw(win)

    is_quit = False

    while not is_quit:
        reset(door_1,door_2,door_3,try_again_text, info_text)

        set_secretdoor(door_1,door_2,door_3)
        mouse_point = win.getMouse()

        if quit_button.is_clicked(mouse_point):
            is_quit = True

        elif door_1.is_clicked(mouse_point):
            if door_1.is_secret():
                wins += 1
                win_button.set_label(wins)
                result(True, door_1,info_text,try_again_text,win)
            else:
                losses += 1
                loss_button.set_label(losses)
                show_secret_door(door_1, door_2, door_3)
                result(False, door_1, info_text, try_again_text, win)

        elif door_2.is_clicked(mouse_point):
            if door_2.is_secret():
                wins += 1
                win_button.set_label(wins)
                result(True, door_2,info_text,try_again_text, win)
            else:
                losses += 1
                loss_button.set_label(losses)
                show_secret_door(door_1, door_2, door_3)
                result(False, door_2,info_text,try_again_text, win)

        elif door_3.is_clicked(mouse_point):
            if door_3.is_secret():
                wins += 1
                win_button.set_label(wins)
                result(True, door_3,info_text,try_again_text, win)
            else:
                losses += 1
                loss_button.set_label(losses)
                show_secret_door(door_1,door_2,door_3)
                result(False, door_3,info_text,try_again_text, win)

main()
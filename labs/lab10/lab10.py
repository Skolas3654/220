from graphics import Point, Rectangle, GraphWin
from button import Button
from door import Door

def main():
    win = GraphWin("Door", 500,500)

    b = Button(Rectangle(Point(200,100),Point(300,150)),"Exit")
    d = Door(Rectangle(Point(100,200),Point(400,500)),"Open")

    b.draw(win)
    d.draw(win)


    button_clicked = False

    door_open = True
    d.color_door('light blue')

    while not button_clicked:
        mouse_point = win.getMouse()
        button_clicked = b.is_clicked(mouse_point)

        if d.is_clicked(mouse_point):
            if door_open == False:
                d.open('light blue','Open')
                door_open = True
            else:
                d.close("brown", 'Close')
                door_open = False

main()
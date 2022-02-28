import graphics

from graphics import Point, Circle, Text, Entry

win = graphics.GraphWin("Face",700,700, True)

face_circle = Circle(Point(350,100),100)
face_circle.setFill("gold")


eye_left_circle = Circle(Point(350,350), 55)
eye_left_circle.setFill("blue")


eye_right_circle = graphics.Circle(Point(400,75), 25)
eye_right_circle.setFill("blue")

mouth_line_1 = graphics.Point(300,150)
mouth_line_2 = graphics.Point(400,150)

mouth = graphics.Line(mouth_line_1,mouth_line_2)

message = Text(Point(350,600),"Test Message")
message.setTextColor("red")


#win.setCoords(0,0,10,10)

face_circle.draw(win)
eye_left_circle.draw(win)
eye_right_circle.draw(win)
mouth.draw(win)

message.draw(win)

user_input = Entry(Point(350,350),50)
user_input.draw(win)
click = win.getMouse()
name = user_input.getText()

print(name)
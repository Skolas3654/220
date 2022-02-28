import graphics
from graphics import Text, GraphWin, Point, Entry

def convert_gui():
    win = GraphWin("converter",700,700)
    win.setCoords(0,0,10,10)
    celsius_text = Text(Point(3,8),"Celsius")
    celsius_entry = Entry(Point(7,8),30)

    click_text = Text(Point(5,5),"Click to close")
    convert_text = Text(Point(8,5),"Result")

    celsius_text.draw(win)
    celsius_entry.draw(win)
    click_text.draw(win)
    convert_text.draw(win)
    win.getMouse()
    celsius = eval(celsius_entry.getText())
    fahrenheit = celsius * 9/5 + 32
    print(fahrenheit)

    click_text.setText(fahrenheit)
    win.getMouse()




convert_gui()
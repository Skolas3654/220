import math

import graphics
from graphics import *

height = 300
width = 400

win = GraphWin("Vigerere",width,height)

code_text = Text(Point(100,50),"Message to code")
code_entry = Entry(Point(225,50),10)

key_text = Text(Point(100,100),"Enter Keyword")
key_entry = Entry(Point(225,100),10)

button = Rectangle(Point(150,150),Point(250,200))
button_text = Text(Point(200,175),"Encode")


code_text.draw(win)
code_entry.draw(win)

key_text.draw(win)
key_entry.draw(win)

button.draw(win)
button_text.draw(win)

win.getMouse()

message = code_entry.getText()
key = key_entry.getText()
key = key * 26
key = key.upper()

message = message.replace(" ","")
message = message.upper()

def encryption(string, k):
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(k[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    return ("".join(encrypt_text))

result_pretext = Text(Point(200,225),"Resulting Message")
result_text = Text(Point(200,245),encryption(message,key))
close_text = Text(Point(200,285),"Click Anywhere to Close Window")

result_text.draw(win)
result_pretext.draw(win)
close_text.draw(win)


win.getMouse()




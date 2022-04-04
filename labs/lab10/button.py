from graphics import Text

class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(),label)

    def get_label(self):
        return  self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        xRange = (self.shape.getP1().getX() <= point.getX() and point.getX() <= self.shape.getP2().getX())
        yRange = (self.shape.getP1().getY() <= point.getY() and point.getY() <= self.shape.getP2().getY())
        return xRange and yRange

    def color_button(self, color):
        self.shape.setFill(color)




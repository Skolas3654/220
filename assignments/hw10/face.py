from graphics import Circle, Line, Polygon, Point
from sphere import Sphere


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)
        self.smile_mouth = Polygon(point_1,point_2,Point(250,320))
        self.shock_mouth = Circle(Point(250,310),eye_size)
        self.wink_eye = Line(Point(200,220),Point(230,220))

    def smile(self):
        self.mouth.undraw()
        self.smile_mouth.draw(self.window)


    def shock(self):
        self.mouth.undraw()
        self.shock_mouth.draw(self.window)

    def wink(self):
        self.mouth.undraw()
        self.left_eye.undraw()
        self.smile_mouth.draw(self.window)
        self.wink_eye.draw(self.window)

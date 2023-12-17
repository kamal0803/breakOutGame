from turtle import Turtle

class Brick(Turtle):

    def __init__(self, x, y, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=2.5)


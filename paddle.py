from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=10)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def within_right_bound(self):
        if self.xcor() > 300:
            self.setx(self.xcor() - 20)

    def within_left_bound(self):
        if self.xcor() < -300:
            self.sety(self.xcor() + 20)
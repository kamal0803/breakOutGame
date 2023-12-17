from turtle import Turtle

class Ball(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

        self.goto(x, y)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = 10
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def bounce_y(self):
        self.y_move = self.y_move * (-1)

    def bounce_x(self):
        self.x_move = self.x_move * (-1)

from turtle import Turtle, Screen
from paddle import Paddle
from brick import Brick
from ball import Ball
import time

screen = Screen()
screen.title("Breakout Game!")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = Paddle(0, -280)
ball = Ball(0, -260)

bricks = []

for i in range(-360, 420, 60):
    bricks.append(Brick(i, 0, "blue"))
    bricks.append(Brick(i, 30, "green"))
    bricks.append(Brick(i, 60, "yellow"))
    bricks.append(Brick(i, 90, "red"))

screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
screen.listen()

game_is_on = True

while game_is_on:

    time.sleep(0.09)
    ball.move()

    # Collision of ball with bricks
    for i in range(len(bricks)):

        if ball.distance(bricks[i]) < 30 and bricks[i].ycor() <= 90:
            x_n = bricks[i].xcor()
            y_n = bricks[i].ycor()
            bricks[i].reset()
            bricks[i].goto(x_n, y_n)
            del bricks[i]

            ball.bounce_y()

        if i == len(bricks) - 1:
            break

    # Collision of ball with side wall
    if abs(ball.xcor()) > 380:
        ball.bounce_x()

    # Collision of ball with upper wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # Collision of ball with bottom wall - GAME OVER!
    if ball.ycor() < -280:
        print("Game Over!")
        game_is_on = False

    # Collision of ball with paddle
    if ball.distance(paddle) < 100 and ball.ycor() < -260:

        if paddle.xcor() > 0:

            if ball.xcor() < paddle.xcor():
                ball.bounce_y()
            else:
                ball.bounce_y()
                ball.bounce_x()

        elif paddle.xcor() < 0:

            if ball.xcor() < paddle.xcor():
                ball.bounce_y()
                ball.bounce_x()
            else:
                ball.bounce_y()

        else:
            ball.bounce_y()

    paddle.within_left_bound()
    paddle.within_right_bound()

    screen.update()

screen.mainloop()


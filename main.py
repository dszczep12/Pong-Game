from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time




# Screen Setup
screen = Screen()
screen.setup(800, 600)
screen.title("Pong_Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


# key movements


screen.listen()
screen.onkey(r_paddle.go_up(), "Up")
screen.onkey(r_paddle.go_down(), "Down")
screen.onkey(l_paddle.go_up(), "w")
screen.onkey(l_paddle.go_down(), "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move

screen.exitonclick()

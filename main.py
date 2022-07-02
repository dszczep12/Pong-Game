from turtle import Turtle, Screen

screen = Screen()

# Screen Setup
screen.setup(800, 600)
screen.title("Pong_Game")
screen.bgcolor("black")


# Paddle Setup L/R
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.speed(0)
paddle.goto(350, 0)

# key movements
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

screen.exitonclick()



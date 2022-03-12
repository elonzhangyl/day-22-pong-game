from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)


screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# Create the ball
ball = Ball()

scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with upper and lower boundaries and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles and bounce
    if ball.distance(right_paddle) < 30 and ball.xcor() == 340:
        ball.bounce_x()
        scoreboard.update_right()
    elif ball.distance(left_paddle) < 30 and ball.xcor() == -340:
        ball.bounce_x()
        scoreboard.update_left()

    # Detect collision with left and right boundaries and lose
    if ball.xcor() > 350 or ball.xcor() < -350:
        game_is_on = False







screen.exitonclick()
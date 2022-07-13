from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.title("Pong Arcade Game")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)


game=True
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
ball=Ball()
score=Scoreboard()

while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Top wall collision
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    #Paddle collision
    if ball.xcor()>320 and ball.distance(r_paddle)<50 or ball.xcor()<-320 and ball.distance(l_paddle)<50:
        ball.paddle_bounce()
    #Right paddle missed the ball
    if ball.xcor()>380:
        ball.refresh()
        score.l_point+=1
        score.updated()
    #Left paddle missed the ball
    if ball.xcor()<-380:
        ball.refresh()
        score.r_point+=1
        score.updated()




screen.exitonclick()
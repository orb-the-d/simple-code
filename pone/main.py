from turtle import Screen
from paddle_1 import Paddle_1
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
score=Score()



paddle_1=Paddle_1(350,0)
paddle_2=Paddle_1(-350,0)
ball=Ball()




screen.listen()
screen.onkey(paddle_1.up,"Up")
screen.onkey(paddle_1.down,"Down")
screen.onkey(paddle_2.up,"w")
screen.onkey(paddle_2.down,"s")


game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()

    #detect collision with the paddle
    if ball.distance(paddle_1)<50 and ball.xcor()>330  or ball.distance(paddle_2)<50 and ball.xcor()<-330 :
        ball.bounce_x()

    if ball.xcor()>380 :
        ball.restart()
        score.l_point()

    if ball.xcor()<-380:
        ball.restart()
        score.r_point()

    if score.score_r==4 or score.score_l==4:
        print(f"game over ")
        score.game_over()
        game_on=False














screen.exitonclick()
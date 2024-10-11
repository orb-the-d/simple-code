from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.mouve()
    #detect crash with food
    if snake.head.distance(food)<15:
        snake.extand()
        food.refresh()
        score.increase()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 :
        score.reset_score()
        snake.reset_snake()

    if snake.hit_body():
        score.reset_score()
        snake.reset_snake()

























screen.exitonclick()
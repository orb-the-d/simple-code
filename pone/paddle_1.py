from turtle import Turtle




class Paddle_1(Turtle):
    def __init__(self,x,y):
        super().__init__("square")
        self.turtlesize(5, 1)
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(x, 0)
        self.score=0






    def up(self):
        y_pos= self.ycor() + 20
        x_pos =self.xcor()
        self.goto(x_pos,y_pos)

    def down(self):
        y_pos= self.ycor() - 20
        x_pos = self.xcor()
        self.goto(x_pos,y_pos)
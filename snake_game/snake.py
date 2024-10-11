from turtle import Turtle

STARTPOS=[(0,0),(-20,0),(-40,0)]
MOUVE_DISTACE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:

    def __init__(self):
        self.segmant=[]
        self.creat_snake()
        self.head=self.segmant[0]




    def creat_snake(self,):
        for startpos in STARTPOS:
            self.add_segmant(startpos)



    def add_segmant(self,startpos):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(startpos)
        self.segmant.append(snake)

    def extand(self):
        self.add_segmant(self.segmant[-1].pos())


    def mouve(self):
        for seg_num in range(len(self.segmant) - 1, 0, -1):
            new_x = self.segmant[seg_num - 1].xcor()
            new_y = self.segmant[seg_num - 1].ycor()
            self.segmant[seg_num].goto(new_x, new_y)
        self.head.forward(MOUVE_DISTACE)

    def hit_body(self):
        for seg in self.segmant[1:]:
            if self.head.distance(seg)==0 :
                return True

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.seth(LEFT)

    def reset_snake(self):
        for seg in self.segmant:
            seg.goto(1000,1000)
        self.segmant.clear()
        self.creat_snake()
        self.head=self.segmant[0]
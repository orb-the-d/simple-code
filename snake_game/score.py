from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        with open("data.txt",mode="r")as file:
            self.high_score=int(file.read())

        self.penup()
        self.goto(0,270)
        self.score_write()
        self.hideturtle()

    def score_write(self):
        self.clear()
        self.write(f" score : {self.score} , high score :{self.high_score}", align="center", font=('Arial', 8, 'normal'))

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w")as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.score_write()


    def increase(self):
        self.score+=1
        self.score_write()

    # def game_over(self):
    #     self.goto((0,0))
    #     self.write("game over",align="center")
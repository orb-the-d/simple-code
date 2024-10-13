from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_r=0
        self.score_l=0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=("courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=("courier", 60, "normal"))


    def l_point(self):
        self.score_l += 1
        self.clear()
        self.update()


    def r_point(self):
        self.score_r +=1
        self.clear()
        self.update()

    def game_over(self):
        self.home()
        self.write("game over ",align="center", font=("courier", 20, "normal"))
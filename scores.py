from turtle import Turtle

class Scores(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.scores_update()

    def scores_update(self):
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 14, "normal"))

    def get_point(self):
        self.score += 1
        self.clear()
        self.scores_update()

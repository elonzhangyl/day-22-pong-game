from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.scoreboard_write()

    def scoreboard_write(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_left, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, align="center", font=("Courier", 80, "normal"))

    def update_left(self):
        self.score_left += 1
        self.scoreboard_write()

    def update_right(self):
        self.score_right += 1
        self.scoreboard_write()

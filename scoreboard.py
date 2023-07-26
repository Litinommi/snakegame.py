from turtle import Turtle
ALLIGNMENT="center"
FONT=("Arial", 10, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(F"SCORE = {self.score} ", align=ALLIGNMENT, font=FONT)

    def game_is_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)


    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


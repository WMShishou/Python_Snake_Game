from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.number_of_points = 0
        self.score()

    def score(self):
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 260)
        self.write(f'Score: {self.number_of_points}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.number_of_points += 1
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=FONT)
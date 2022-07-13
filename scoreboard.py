from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_point=0
        self.r_point=0
        self.updated()


    def updated(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f" {self.l_point}",align="center",font=("Courier", 40, "bold"))
        self.goto(100, 200)
        self.write(f" {self.r_point}",align="center", font=("Courier", 40, "bold"))
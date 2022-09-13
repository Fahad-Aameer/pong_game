from turtle import Turtle


class Player(Turtle):
    def __init__(self, pos1, pos2):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.resizemode("user")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(pos1, pos2)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

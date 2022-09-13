from turtle import Turtle


class Line:

    def __init__(self):
        self.lines = Turtle()
        self.lines.penup()
        self.lines.speed('fastest')
        self.lines.goto(0, 300)
        self.lines.right(90)
        self.lines.pencolor("white")
        self.lines.pendown()
        for i in range(30):
            self.lines.forward(20)
            self.lines.penup()
            self.lines.forward(20)
            self.lines.pendown()

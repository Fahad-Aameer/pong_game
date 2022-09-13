from turtle import Screen
from lines import Line
from players import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
line = Line()
ball = Ball()
score = Scoreboard()
player1 = Player(350, 0)
player2 = Player(-350, 0)
screen.listen()
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")

game_on = True
while game_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 400:
        ball.refresh()
        ball.bounce_x()
        time.sleep(1)
        score.l_point()
    if ball.xcor() < -400:
        ball.refresh()
        ball.bounce_x()
        time.sleep(1)
        score.r_point()

screen.exitonclick()

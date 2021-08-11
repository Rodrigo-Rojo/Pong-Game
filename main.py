from turtle import Screen
from divider import Divider
from scoreboard import Score
from player import Player
from computer import Computer
from ball import Ball
import time

screen = Screen()
screen.setup(width=900, height=500)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

divider = Divider()
score = Score()
player = Player()
computer = Computer()
ball = Ball()
screen.onkeypress(player.up, "w")
screen.onkeypress(player.down, "s")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.03)
    ball.move()
    ball.control_ball_heading()
    player.ball_interact(ball)
    computer.ball_interact(ball)
    ball.check_if_score(score)
    computer.bot_ia(ball)
screen.exitonclick()

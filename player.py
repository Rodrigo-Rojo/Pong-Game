from turtle import Turtle
import random


class Player:
    def __init__(self):
        self.player = []
        self.create_player()

    def create_player(self):
        position = 40
        for _ in range(4):
            player = Turtle(shape="square")
            player.color("white")
            player.penup()
            player.goto(x=-437, y=position)
            position -= 20
            self.player.append(player)

    def up(self):
        if self.player[0].ycor() > 230:
            pass
        else:
            for body in self.player:
                body.setheading(90)
                body.forward(20)

    def down(self):
        if self.player[-1].ycor() < -230:
            pass
        else:
            for body in self.player:
                body.setheading(270)
                body.forward(20)

    def ball_interact(self, ball):
        for body in self.player:
            if ball.distance(body) < 20:
                ball.setheading(0 + random.randint(-45, 45))
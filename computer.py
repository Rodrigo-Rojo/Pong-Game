from turtle import Turtle
import random


class Computer:
    def __init__(self):
        self.computer = []
        self.create_computer()
        self.number = 0

    def create_computer(self):
        position = 40
        for _ in range(5):
            computer = Turtle(shape="square")
            computer.color("white")
            computer.penup()
            computer.goto(x=430, y=position)
            position -= 20
            self.computer.append(computer)

    def up(self):
        if self.computer[0].ycor() > 230:
            pass
        else:
            for body in self.computer:
                body.setheading(90)
                body.forward(20)

    def down(self):
        if self.computer[-1].ycor() < -230:
            pass
        else:
            for body in self.computer:
                body.setheading(270)
                body.forward(20)

    def ball_interact(self, ball):
        for body in self.computer:
            if ball.distance(body) < 20:
                ball.setheading(180 + random.randint(-45, 45))

    def bot_ia(self, ball):
        if self.number == 3:
            if ball.ycor() > self.computer[2].ycor():
                self.up()
            else:
                self.down()
            self.number = 0
        self.number += 1

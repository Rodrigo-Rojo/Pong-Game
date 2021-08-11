from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed(1)
        self.left_or_right()
        self.control_ball_heading()

    def left_or_right(self):
        self.goto(0, 0)
        random_choice = random.randint(0, 2)
        if random_choice == 0:
            self.setheading(random.randint(135, 225))
        else:
            self.setheading(random.randint(315, 405))

    def move(self):
        self.forward(10)

    def control_ball_heading(self):
        if -240 < self.ycor() > 240:
            self.setheading(0 - self.heading())
        elif self.ycor() < -240:
            self.setheading(0 - self.heading())

    def check_if_score(self, score):
        if self.xcor() > 440:
            score.score_user()
            self.left_or_right()
        elif self.xcor() < -440:
            score.bot_score()
            self.left_or_right()
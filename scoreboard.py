from turtle import Turtle


class Score:
    def __init__(self):
        self.score = []
        self.create_turtle()
        self.user1 = self.score[0]
        self.user2 = self.score[1]
        self.user1_score = 0
        self.user2_score = 0
        self.create_scoreboard()

    def create_turtle(self):
        for index in range(2):
            turtle = Turtle()
            turtle.penup()
            turtle.hideturtle()
            turtle.pencolor("white")
            self.score.append(turtle)

    def score_user(self):
        self.user1.clear()
        self.user1_score += 1
        self.create_scoreboard()

    def bot_score(self):
        self.user2.clear()
        self.user2_score += 1
        self.create_scoreboard()

    def create_scoreboard(self):
        self.user1.goto(x=-40, y=200)
        self.user1.write(arg=f"{self.user1_score}", align="center", move=True, font=("Courier", 30, "bold"))
        self.user2.goto(x=45, y=200)
        self.user2.write(arg=f"{self.user2_score}", align="center", move=True, font=("Courier", 30, "bold"))
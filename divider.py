from turtle import Turtle


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.color("red")
        self.pencolor("white")
        self.pensize(3)
        self.penup()
        self.goto(x=0, y=250)
        self.setheading(270)
        self.set_divider()
        self.set_user_name()
        self.set_bot_name()
        self.hideturtle()

    def set_divider(self):
        for _ in range(25):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def set_user_name(self):
        self.goto(x=-230, y=230)
        self.write(arg="Player 1", align="center", move=True, font=("Courier", 16, "bold"))

    def set_bot_name(self):
        self.goto(x=230, y=230)
        self.write(arg="IA", align="center", move=True, font=("Courier", 16, "bold"))

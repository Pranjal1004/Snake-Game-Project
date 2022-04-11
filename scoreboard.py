from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.color("white")
        self.current_score = 0
        with open("data.txt") as file:
            content = int(file.read())
            self.high_score = content
        self.update_score()
        self.penup()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.current_score}  High Score: {self.high_score}", move=False, align="center",
                   font=("courier", 15, "normal"))

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.current_score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", move=False, align="center", font=("courier", 15, "normal"))

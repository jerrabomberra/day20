from turtle import Screen, Turtle


screen = Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.game_score = 0
        self.score = Turtle()
        self.penup()
        self.game_score += 1

    def keep_score(self):
        
        while self.game_score < 10:
            self.score.write(f"Score :{self.game_score}", True, align="center")
            break

x = Scoreboard()
x.keep_score()
screen.exitonclick()


from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.file = open("highscore.txt",mode="r")
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(0,260)
        self.highscore = int(self.file.read())
        self.file.close()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore}",align="center",font=("Courier",24,"normal"))


    def save(self):
        with open("snakeGame\highscore.txt", mode="w") as file:
            file.write(str(self.highscore))

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save() 
        self.score = 0
        self.update_scoreboard()
        
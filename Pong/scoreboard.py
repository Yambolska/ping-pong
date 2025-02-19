from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.scoreboard()


    def scoreboard(self):
        self.teleport(-100, 220)
        self.write(arg=self.l_score, align='center', font=('Arial', 70, 'normal'))
        self.teleport(100, 220)
        self.write(arg=self.r_score, align='center', font=('Arial', 70, 'normal'))



    def r_point(self):
        self.clear()
        self.r_score+=1
        self.scoreboard()



    def l_point(self):
        self.clear()
        self.l_score+=1
        self.scoreboard()

    def finish(self):
        self.clear()
        self.color('black')
        if self.l_score==5:
            self.write(arg='winner left side', align='center', font=('Arial', 70, 'normal'))
        if self.r_score==5:
            self.write(arg='winner right side', align='center', font=('Arial', 70, 'normal'))







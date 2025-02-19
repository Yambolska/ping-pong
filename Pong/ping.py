from turtle import Turtle
class Pong(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.teleport(position,0)

    def up(self):
        self.penup()
        if self.ycor() < 250 :
            self.goto(self.xcor(),self.ycor()+25)

    def down(self):
        self.penup()
        if self.ycor()>-250:
            self.goto(self.xcor(), self.ycor() -25)

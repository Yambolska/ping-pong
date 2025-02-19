from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.home()
        self.penup()
        self.x=4
        self.y=4


    def move(self,):
        x=self.xcor()+self.x
        y=self.ycor()+self.y
        self.goto(x,y)

    def bounce(self):
        self.y*=-1

    def p_bounce(self):
        self.x*=-1

    def fast(self):
        self.x*=1.18

    def restart(self,direction):
        self.teleport(x=0, y=0)
        self.x = 3 * direction
        self.move()



















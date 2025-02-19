from turtle import Turtle,Screen
from ping import Pong
from ball import Ball
from scoreboard import ScoreBoard
import time

turtle=Turtle()
scoreboard=ScoreBoard()
screen=Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800, height=600)
turtle.teleport(0,-290)
turtle.color('white')
turtle.left(90)
turtle.pensize(10)

for i in range (0,25):
    turtle.pendown()
    turtle.forward(12)
    turtle.penup()
    turtle.forward(12)

turtle.hideturtle()
ball=Ball()
r_ping=Pong(370)
l_ping=Pong(-370)
screen.listen()
screen.onkey(r_ping.up,'Up')
screen.onkey(r_ping.down,'Down')
screen.onkey(l_ping.up,'w')
screen.onkey(l_ping.down,'s')
game=True
while game:
    time.sleep(0.001)
    screen.update()
    ball.move()
    if ball.ycor()>285 or ball.ycor()<-285:
        ball.bounce()

    if ball.xcor()>400:
        scoreboard.l_point()
        if scoreboard.l_score==5:
            screen.clear()
            scoreboard.finish()
            game=False
        ball.restart(-1)

    if ball.xcor()<-400:
        scoreboard.r_point()
        if scoreboard.r_score==5:
            screen.clear()
            scoreboard.finish()
            game=False
        ball.restart(1)

    if ball.xcor()>350 and ball.distance(r_ping)<50:
        ball.p_bounce()
        ball.fast()

    if ball.xcor()<-350 and ball.distance(l_ping)<50:
        ball.p_bounce()
        ball.fast()








screen.exitonclick()
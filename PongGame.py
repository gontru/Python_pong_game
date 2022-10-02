# Simple Pong Game

import turtle
import winsound

# setup of window on turtle module or use pi game

window = turtle.Screen()
window.title("Pong by Gonzalo T",)
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


# Score
score_a = 0
score_b = 0


# Paddle A
# turtle object
paddle_A = turtle.Turtle()
# animation speed
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)

# Paddle B
# turtle object
paddle_B = turtle.Turtle()
# animation speed
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

# Ball
# turtle object
ball = turtle.Turtle()
# animation speed
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.Dx = .08
ball.Dy = .08

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))




# Functions
def paddle_A_Up():
    # finding y coordinate using ycor from turtle and assigning it to y
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_Down():
    # finding y coordinate using ycor from turtle and assigning it to y
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_B_Up():
        # finding y coordinate using ycor from turtle and assigning it to y
        y = paddle_B.ycor()
        y += 20
        paddle_B.sety(y)

def paddle_B_Down():
        # finding y coordinate using ycor from turtle and assigning it to y
        y = paddle_B.ycor()
        y -= 20
        paddle_B.sety(y)


# Keyboard binding uses functions
window.listen()
window.onkeypress(paddle_A_Up, "w")
window.onkeypress(paddle_A_Down, "s")
# paddle B
window.onkeypress(paddle_B_Up, "Up")
window.onkeypress(paddle_B_Down, "Down")




# Main game loop

while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.Dx)
    ball.sety(ball.ycor() + ball.Dy)


# Border checking
#compare y cord
    if ball.ycor() > 290:
        ball.sety(290)
        ball.Dy *= -.05
        #os.system("aplay bounce.wav&") for linux
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.Dy *= -.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.Dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.Dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40):
        ball.setx(340)
        ball.Dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40):
        ball.setx(-340)
        ball.Dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


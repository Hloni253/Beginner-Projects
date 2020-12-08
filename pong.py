import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

pa = turtle.Turtle()
pa.speed(0)
pa.penup()
pa.goto(-350, 0)
pa.color("white")
pa.shape("square")
pa.shapesize(stretch_wid=5, stretch_len=1)

pb = turtle.Turtle()
pb.speed(0)
pb.penup()
pb.goto(350, 0)
pb.color("white")
pb.shape("square")
pb.shapesize(stretch_wid=5, stretch_len=1)

ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.color("white")
ball.shape("square")
ball.dx = 0.7
ball.dy = 0.7

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0,240)
pen.write("Player A: 0 - Player B: 0 ", align="center" ,font=("Courier", 24, "normal"))

p = turtle.Turtle()
p.penup()
p.hideturtle()
p.color("white")


def pa_up():
    y = pa.ycor()
    y += 20
    pa.sety(y)
    
def pa_down():
    y = pa.ycor()
    y -= 20
    pa.sety(y)
    
def pb_up():
    y = pb.ycor()
    y += 20
    pb.sety(y)
    
def pb_down():
    y = pb.ycor()
    y -= 20
    pb.sety(y)
    
wn.listen()
wn.onkeypress(pa_up, 'd')
wn.onkeypress(pa_down, 'c')
wn.onkeypress(pb_up, 'Up')
wn.onkeypress(pb_down, 'Down')


while True:
    wn.update()
    
    if pb.ycor() > 250:
        pb.sety(250)
        
    if pb.ycor() < -250:
        pb.sety(-250)
        
    if pa.ycor() > 250:
        pa.sety(250)
        
    if pa.ycor() < -250:
        pa.sety(-250)
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
       
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} - Player B: {} ".format(score_a, score_b), align="center" ,font=("Courier", 24, "normal"))
        if score_a == 5:
            p.write("GAME OVER\nPlayer One Wins", align="center", font=("Courier", 50, "bold"))
            break

        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} - Player B: {} ".format(score_a, score_b), align="center" ,font=("Courier", 24, "normal"))
        if score_b == 5:
            p.write("GAME OVER\nPlayer Two Wins", align="center", font=("Courier", 50, "bold"))
            break

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pb.ycor() + 50 and ball.ycor() > pb.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pa.ycor() + 50 and ball.ycor() > pa.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
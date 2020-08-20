

import turtle

#game setup
board = Turtle.Screen()
board.tittle("welcome friends hope you like it ")
board.bgcolor("black")
board.setup(width=800, height=600)
board.tracer(0)

#raquet 1
raquet_1 = turtle.Turtle()
raquet_1.speed(0)
raquet_1.shape("square")
raquet_1.color("red")
raquet_1.shapesize(stretch_wid=5, stretch_len=1)
raquet_1.penup()
raquet_1.goto(-350, 0)


#raquet 2
raquet_2 = turtle.Turtle()
raquet_2.speed(0)
raquet_2.shape("square")
raquet_2.color("blue")
raquet_2.shapesize(stretch_wid=5, stretch_len=1)
raquet_2.penup()
raquet_2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

#movement
def raquet_1_up:
	y = raquet_1.ycor()
	y += 20
	raquet_1.sety(y)

def raquet_1_down:
	y = raquet_1.ycor()
	y -= 20
	raquet_1.sety(y)

def raquet_2_up:
	y = raquet_2.ycor()
	y += 20
	raquet_2.sety(y)

def raquet_2_down:
	y = raquet_2.ycor()
	y -= 20
	raquet_2.sety(y)

#keyboard
board.lisen()
board.onkeypress(raquet_1_up, "w")  	
board.onkeypress(raquet_1_down, "s")  
board.onkeypress(raquet_2_up, "Up")  	
board.onkeypress(raquet_2_down, "Down")  

#ball movement
ball.setx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)

#loop
while True:
	board.update()

	#ball movement
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	
	#boders board
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() > -290:
		ball.sety(-290)
		ball.dy *= -1

	#return ball to mid	
	if ball.xcor()>390:
		ball.goto(0, 0)
		ball.dx *= -1

	if ball.xcor()< -390:
		ball.goto(0, 0)
		ball.dx *= -1

	#racquets hit
	if ball.xcor() >340 and (ball.ycor() < raquet_2l.ycor() + 50 and ball.ycor() > raquet_2.ycor() -50):

import turtle
import random
import time

# Game configuration
delay = 0.001
score = 0
high_score = 0

# Creating a body for the snake
bodies = []

# Creating a screen
s1 = turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("light blue")
s1.setup(width=600, height=600)

# Creating the snake's head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Creating the food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.penup()
food.ht()
food.st()
food.goto(250, 200)

# Creating a score card
score_display = turtle.Turtle()
score_display.ht()
score_display.penup()
score_display.goto(-250, 250)
score_display.write("Score:0 | High Score:0", font=("Arial", 16, "bold"))
# Functions to control the snake's movement
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def moveStop():
    head.direction = "stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
#Event Handling
s1.listen()
s1.onkey(moveUp,"Up")
s1.onkey(moveDown,"Down")
s1.onkey(moveLeft,"Left")
s1.onkey(moveRight,"Right")
s1.onkey(moveStop,"space")
#main loop:
while(True):
    s1.update()
    #check collision with border:
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)
    #Check if Collision with food:
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #Increase Length of Snake:
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("green")
        bodies.append(body)
        #Increase Score card:
        score=score+100
        if score>high_score:
            high_score=score
        score_display.clear()
        score_display.write("Score:{}|High Score:{}".format(score,high_score))
        delay=delay+0.005
    #move Snake Bodies:
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
    #check if Collision with Snake Body:
    for b in bodies:
        if b.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for b in bodies:
                b.ht()
            bodies.clear()
            score=0
            delay=0.1
            score_display.write("Score:{}|High Score:{}".format(score,high_score))
            time.sleep(delay)
#Run into Infinite loop Game:
s1.mainloop()
import turtle
import os
import math

from pip._vendor.distlib.compat import raw_input

wn= turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invader")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.down()
border_pen.pensize(3)
for size in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

# Create player
player = turtle.Turtle()
player.shape("triangle")
player.color("#00ff00")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed= 15
# create enemy
enemy = turtle.Turtle()
enemy.color("#ff3333")
enemy.shape("circle")
enemy.speed(0)
enemy.penup()
enemy.setposition(-200, 250)
enemyspeed = 2

# Creating player's bullets
bullet = turtle.Turtle()
bullet.color("#ffff1a")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# defining bullet state
# ready bullet - ready to fire
# fire bullet - firing
bulletstate = "ready"

# move left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    # fire and move it towards invaders
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor()- t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# keyboard binding
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

while True:
    wn.update()

    # move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    # move and back down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # new bullet firing
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    # collision between bullet and enemy

    if isCollision(bullet, enemy):
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        enemy.setposition(-200, 250)

    if isCollision(player, enemy):
        enemy.hideturtle()
        player.hideturtle()
        print("Game Over!")
        break

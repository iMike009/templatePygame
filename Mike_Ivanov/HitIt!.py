from turtle import *
from time import sleep

class Sprite(Turtle):
    def __init__(self,x,y,step,shape,color):
        super().__init__()
        self.penup()
        self.speed()
        self.goto(x,y)
        self.color(color)
        self.shape(shape)
        self.step = step
    
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
    
    def is_collide(self,sprite):
        dist = self.distance(sprite.xcor(),sprite.ycor())
        if dist < 20:
            return True 
        else:
            return False
    
    def set_move(self,x_start,y_start,x_end,y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start,y_start)
        self.setheading(self.towards(x_end,y_end))
    
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end,self.y_end) < self.step:
            self.set_move(self.x_end,self.y_end,self.x_start,self.y_start)
    
player = Sprite(0, -100, 10, 'circle', 'orange')
point = Sprite(0, 150, 10, 'triangle', 'green')
enemy1 = Sprite(-200, 60, 20, 'square', 'red')
enemy1.set_move(-200,60, 200,-60,)
enemy2 = Sprite(200, -60, 20, 'square', 'red')
enemy2.set_move(-200,-60, 200,60)
enemy3 = Sprite(-200,0,20,'square','red')
enemy3.set_move(-200,0, 200,0)

scr = player.getscreen()
scr.listen()

scr.onkey(player.move_up, 'w')
scr.onkey(player.move_down, 's')
scr.onkey(player.move_left, 'a')
scr.onkey(player.move_right, 'd')

score = 0

while score < 3:
    enemy1.make_step()
    enemy2.make_step()
    enemy3.make_step()
    if player.is_collide(point):
        score +=1
        player.goto(0,-100)
    if player.is_collide(enemy1) or player.is_collide(enemy2) or player.is_collide(enemy3):
        point.hideturtle()
        break
enemy1.hideturtle()
enemy2.hideturtle()
enemy3.hideturtle()

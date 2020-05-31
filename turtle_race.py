from turtle import *
from random import randint
speed(0)
penup()
goto(-140,140)
for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(30)
  penup()
  forward(30)
  pendown()
  forward(30)
  penup()
  forward(30)
  pendown()
  forward(30)
  penup()
  backward(160)
  left(90)
  forward(20)

ada=Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto((-160,115))
ada.pendown()


bob=Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,55)
bob.pendown()

leo=Turtle()
leo.color('green')
leo.shape('turtle')

leo.penup()
leo.goto(-160,-5)
leo.pendown()

for turn in range(10):
  ada.right(36)
  bob.right(36)
  leo.right(36)


for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  leo.forward(randint(1,5))

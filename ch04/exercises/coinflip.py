import turtle
import random


turtle.screensize(100,100)

myturtle = turtle.Turtle()
myturtle.shape("turtle")
myturtle.color('blue')


while myturtle.xcor()<= 100 and myturtle.ycor() <= 100:
  number = random.randrange(1,10)
  remainder = number%2

  if remainder == 1:
    print("coin flip: head")
    myturtle.left(90)
    myturtle.forward(50)


  elif remainder == 0:
    print("coin flip: tail")
    myturtle.right(90)
    myturtle.forward(50)


  elif myturtle.xcor()>100 or myturtle.ycor()>100:
    break
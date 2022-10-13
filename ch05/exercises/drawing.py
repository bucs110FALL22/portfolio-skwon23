import turtle
myturtle = turtle.Turtle()
num_sides = int()
side_length = float()


def drawEqShape(myturtle,num_sides,side_length):
  
  
  
  myturtle.shape("turtle")
  myturtle.color('green')
  myturtle.down()
  
  num_sides = input("What is the number of sides?")
  side_length = input("what is the side length?")

  angle = (360 / int(num_sides))



  for _ in range(int(num_sides)):

    myturtle.forward(float(side_length))
    myturtle.left(float(angle))


drawEqShape(myturtle,num_sides,side_length)


turtle.exitonclick()

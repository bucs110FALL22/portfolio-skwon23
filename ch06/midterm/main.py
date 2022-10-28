import turtle

turtle.screensize(500,500)
myturtle = turtle.Turtle()
myturtle.shape("turtle")


def main(color,radius, radius2):

  myturtle.up()
  myturtle.goto(-50,50)
  
  myturtle.color(color)
  myturtle.down()
  
  myturtle.fillcolor(color)
  myturtle.begin_fill()
  myturtle.circle(radius)
  myturtle.end_fill()
  myturtle.up()
  myturtle.goto(150,50)

  myturtle.down()
  myturtle.fillcolor(color)
  myturtle.begin_fill()
  myturtle.circle(radius2)
  myturtle.end_fill()

  
  myturtle.up()
  myturtle.right(180)
  myturtle.goto(120,-100)

  myturtle.down()

  myturtle.fillcolor(color)
  myturtle.begin_fill()
  for _ in range(5):
    
  
    for _ in range(3):
      myturtle.forward(30)
      myturtle.left(120)
      
  
  

    myturtle.forward(30)

  myturtle.end_fill()




def head(color,radius3):

  myturtle.up()
  myturtle.goto(55,-300)
  myturtle.color(color)
  myturtle.down()
  myturtle.fillcolor(color)
  myturtle.begin_fill()
  myturtle.circle(radius3)
  myturtle.end_fill()







def side_length(side_length):
  side_length = int(input("What is the length of a side for a nose?"))

  return side_length








  
def nose(side_length):
  myturtle.up()
  myturtle.goto(90,0)
  myturtle.down()
  for _ in range(2):
    myturtle.fillcolor()
    myturtle.begin_fill()
    for _ in range(3):

      
      myturtle.forward(side_length)
      myturtle.right(120)
      
    myturtle.end_fill()
  
    myturtle.forward(side_length)






color = input("please enter a color")
radius3 = int(input("Please enter the radius of head(more than 300 is recommended."))


head(color,radius3)






color = input("Please enter a color")

radius = int(input("Please enter the first eye's radius"))

radius2 = int(input("Please enter the second eye's radius"))




main(color,radius,radius2)



side_length = side_length(side_length)

nose(side_length)






turtle.exitonclick()
from turtle import *
screensize(70,70)

color('blue')
shape("turtle")
down()
number_of_sides = input("what is the number of sides?")
length_of_side = input("what is the length of a side?")


angle = (360 / float(number_of_sides))

n = number_of_sides

for _ in range(int(n)):

  forward(float(length_of_side))
  left(float(angle))


exitonclick()
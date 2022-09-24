import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
x = random.randrange(1,100)
y = random.randrange(1,100)

michelangelo.forward(x)
leonardo.forward(y)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


for _ in range(10):
  z = random.randrange(1,10)
  a = random.randrange(1,10)
  michelangelo.forward(z)
  leonardo.forward(a)

  
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


# PART B - complete part B here

pygame.init()
surface = pygame.display.set_mode((700,500))
pygame.Color(0, 0, 0)


pygame.draw.polygon(surface, 'blue', [(100,50),(200,50),(150,136.6)])

pygame.display.flip()
surface.fill('black')
pygame.time.wait(1000)


pygame.draw.rect(surface, 'blue',(40,80,100,100))

pygame.display.flip()
surface.fill('black')
pygame.time.wait(1000)



coords = []
num_sides = 6
side_length = 50
offset = 100


n = 6
i = 10
for _ in range(n):
  
  theta = (2.0 * math.pi * i ) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset 
  coords.append((x,y))
  i += 11



pygame.draw.polygon(surface, 'blue', coords)

pygame.display.flip()
surface.fill('black')
pygame.time.wait(1000)




coords = []
num_sides = 9
side_length = 50
offset = 100


n = 9
i = 10
for _ in range(n):
  
  theta = (2.0 * math.pi * i ) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset 
  coords.append((x,y))
  i += 11



pygame.draw.polygon(surface, 'blue', coords)


pygame.display.flip()
surface.fill('black')
pygame.time.wait(1000)




coords = []
num_sides = 360
side_length = 50
offset = 100


n = 360
i = 10
for _ in range(n):
  
  theta = (2.0 * math.pi * i ) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset 
  coords.append((x,y))
  i += 11



pygame.draw.polygon(surface, 'blue', coords)

pygame.display.flip()


window.exitonclick()

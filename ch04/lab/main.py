import pygame
import random
import math

pygame.init()


width = 600
height = 300
screen = pygame.display.set_mode([width, height])
pygame.display.get_window_size()

aliceblue = [0,50,0]
blueviolet = [1,57,0]
black = [1,1,0]
coral = [0,50,0]
red = [255,0,0]
blue = [0,50,0]



#part 1
pygame.draw.rect(screen, 'aliceblue', (0,0,300,300))
pygame.draw.circle(screen, 'blueviolet', (150,150),150)
pygame.draw.line(screen, 'black', (150,0),(150,300))
pygame.draw.line(screen, 'black', (0,150),(300,150))



#part 2
for _ in range(10):
    n = 0
    x_coord = random.randrange(0,300)
    y_coord = random.randrange(0,300)
    distance_from_center = math.hypot(150 - x_coord, 150 - y_coord)

    


  
    if distance_from_center <= 300/2:
      n += 1
      pygame.draw.circle(screen,red,(x_coord,y_coord),5)
      print("Player blue throws..... hit")



    elif distance_from_center > 300/2:

      pygame.draw.circle(screen,blue,(x_coord,y_coord),5)
      print("Player blue throws......miss")


    
    pygame.display.flip()
    pygame.time.wait(1000)





width = 600
height = 300
screen = pygame.display.set_mode([width, height])
pygame.display.get_window_size()

aliceblue = [0,50,0]
blueviolet = [1,57,0]
black = [1,1,0]
coral = [0,50,0]
red = [255,0,0]
blue = [0,50,0]



pygame.draw.rect(screen, 'blue', (0,0,300,300))
pygame.draw.rect(screen, 'red', (300,300,300,300))

pygame.display.flip()



player_selection = int()
print("Choose your player.")


o = 0

while o == 0:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      [mx, my] = pygame.mouse.get_pos()
      if mx< 300 :
          o += 1
          player_selection = 1
          print("you selected player blue.")
      elif mx >= 300 :
          o += 1
          player_selection = 2
          print("you selected player red.")

pygame.time.wait(800)  
    


  
    






pygame.draw.rect(screen, 'aliceblue', (0,0,300,300))
pygame.draw.circle(screen, 'blueviolet', (150,150),150)
pygame.draw.line(screen, 'black', (150,0),(150,300))
pygame.draw.line(screen, 'black', (0,150),(300,150))
    
pygame.draw.rect(screen, 'white', (300,300,300,300))
pygame.draw.circle(screen, 'blueviolet', (450,150),150)
pygame.draw.line(screen, 'black', (450,0),(450,300))
pygame.draw.line(screen, 'black', (300,150),(600,150))


pygame.display.flip()
pygame.time.wait(1000)




for _ in range(10):
    n = 0
    x_coord = random.randrange(0,300)
    y_coord = random.randrange(0,300)
    distance_from_center = math.hypot(150 - x_coord, 150 - y_coord)

    a = 0
    x_coord2 = random.randrange(300,600)
    y_coord2 = random.randrange(0,300)
    distance_from_center2 = math.hypot(450 - x_coord2, 450 - y_coord2)


  
    if distance_from_center <= 300/2:
      n += 1
      pygame.draw.circle(screen,red,(x_coord,y_coord),5)
      print("Player blue throws..... hit")



    elif distance_from_center > 300/2:

      pygame.draw.circle(screen,blue,(x_coord,y_coord),5)
      print("Player blue throws......miss")


  
    if distance_from_center2 <= 300/2:
      a += 1
      pygame.draw.circle(screen,red,(x_coord2,y_coord2),5)
      print("Player red throws..... hit")



    elif distance_from_center2 > 300/2:

      pygame.draw.circle(screen,blue,(x_coord2,y_coord2),5)
      print("Player red throws......miss")

    
    pygame.display.flip()
    pygame.time.wait(1000)




if player_selection == 1:
  if n > a:
    print("You assumed correctly.")
  elif n < a:
    print("You assumed wrong.")
  elif n == a:
    print("tie")
elif player_selection == 2:
  if a > n:
    print("You assumed correctly.")
  elif a < n:
    print("You assumed wrong.")
  elif n == a:
    print("tie")





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
    
    


  














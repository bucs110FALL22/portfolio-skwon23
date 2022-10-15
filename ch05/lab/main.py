import pygame

pygame.init()

max_so_far = int()
max_val = int()
n = 101
remainder = n%2
upper_limit = int()
iters = {}
start = 2
iters_key = int()


upper_limit = input("What is the upper limit?")

for n in range(start,int(upper_limit)):
  iters_key = n
  count = 0
  remainder = n%2
  
  while remainder == 1:
    
    n = n * 3 + 1
    print(n)
    count += 1
    print(count)
    remainder = n%2
    if n == 1:
        iters[iters_key] = count
        break
    
    
    
    while remainder == 0:
        
      n = n / 2
      print(n)
      count += 1
      print(count)
      remainder = n%2
      if n == 1:
        iters[iters_key] = count
        break


        
    if n == 1:
      iters[iters_key] = count
      break

  while remainder == 0:
    
    n = n / 2
    print(n)
    count += 1
    print(count)
    remainder = n%2
    if n == 1:
      iters[iters_key] = count
      break
    
    
    
    while remainder == 1:
        
      n = n * 3 + 1
      print(n)
      count += 1
      print(count)
      remainder = n%2
      if n == 1:
        iters[iters_key] = count
        break


        
    if n == 1:
      iters[iters_key] = count
      break
  
  


  



scale = 10
display = pygame.display.set_mode([500,300])
pygame.display.get_window_size()

blue = [0,50,0]



coords = list(iters.items())




print(coords)




a = 0
b = 1

for _ in range(len(coords) - 1):
  
  
  pygame.draw.lines(display, 'blue', False, [(coords[a][0]*scale,coords[a][1]*scale),(coords[b][0]*scale,coords[b][1]*scale)])
  
  a = a + 1
  b = b + 1


new_display = pygame.transform.flip(display, False, True)
display.blit( new_display , (0, 0) )
pygame.display.flip()



b = 0
for _ in range(len(coords) - 1):
  
  if coords[b+1][1] > coords[b][1]:
    max_val = coords[b+1][1]
    max_so_far = coords[b+1][1]
  b += 1



font = pygame.font.Font(None, 50)
msg_str = 'max_so_far:', max_val
msg = font.render(str(msg_str), True, 'blue')
display.blit(msg, (10,10))
pygame.display.flip()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
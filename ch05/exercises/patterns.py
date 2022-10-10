def star_pyramid():
  

  print("How many rows?")
  num_rows = input(int())

  n = 1
  for _ in range(int(num_rows)):
  
  
    for _ in range(n):
    
      print("*")
    
    n += 1


    print("\n")


def rstar_pyramid():
  print("How many rows?")
  num_rows = input(int())

  n = num_rows
  for _ in range(int(num_rows)):
  
  
    for _ in range(int(n)):
    
      print("*")
    
    n = int(n) - 1

    print("\n")
   

star_pyramid()
rstar_pyramid()
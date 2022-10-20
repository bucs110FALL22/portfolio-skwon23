n = int()
a = int()
result = int()
num = int()
exponent = int()



def multiplication(n = int(),a = int(),result = int()) :
  
  result = n
  for _ in range(int(a) - 1):
    
    
    result = result + n


  return result
  
def exponentiation(num,exponent,result):
  
  num = int(input("Enter a number"))
  exponent = int(input("Enter a number"))
  result = num
  for _ in range(int(exponent) - 1):
    result = result * num
    
  return result

x = int()

def square(x,result):

  x = int(input("Enter a number"))
  
  result = multiplication(x,x,result) 

  print(result)
  

square(x,result)



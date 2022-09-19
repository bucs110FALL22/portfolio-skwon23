import random
num = random.randrange(1,10)
num_guesses = 0

n = 3

for _ in range(n):
  guessnum = int(input("PLease guess a number."))
  num_guesses += 1
  if num < guessnum:
    print("Too high")

  elif num > guessnum:
    print("Too low")

  elif num == guessnum:
    print("Correct. You took you", num_guesses,"to get it right.")
    
    break



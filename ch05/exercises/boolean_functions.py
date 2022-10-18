percent = float()
user_score = float()
user_letter = ''


def percent_to_letter(percent,user_letter):
  
  if float(percent) >= 90:
    
    user_letter = 'A'
    
  if float(percent) > 80 and float(percent) < 90:

    user_letter = 'B'
    
  if float(percent) > 70 and float(percent) < 80:
    
    user_letter = 'C'
    
  if float(percent) > 60 and float(percent) < 70:

    user_letter = 'D'
    
  if float(percent) < 60:

    user_letter = 'F'

  return user_letter



def is_passing(user_letter):
  
  if user_letter == 'A':
    return True
    
  if user_letter == 'B':
    return True
    
  if user_letter == 'C':
    return  True
    
  if user_letter == 'D':
    return False
    
  if user_letter == 'F':
    return False


user_score = input("What is your score?")

user_letter = percent_to_letter(user_score,user_letter)

print(user_letter)

print("Is it passing?:",is_passing(user_letter))







class StringUtility:
  
  def __init__(self,string):
    self.string = string
    
    
  """
  This function takes a string in.
  """
  
  def __str__(self):
    
    
    return self.string

  """
  This function returns a string.
  """
  
  def vowels(self):

    vowels = "aeiouAEIOU"
    
    count = 0
    for char in self.string:
      
      if char in vowels:
        count += 1
        
      if count >= 5:

        count = "many"
        break
    
    
      
    count = str(count)  
    return count
        
  """
  This function counts the number of vowels in a string.
  return the number of vowels
  """  
    

  def bothEnds(self):
    if len(self.string) < 2:
        return ''
    else:
        return self.string[0:2] + self.string[-2:]

  """
  This function returns a string made of the first and last two letters of the original string. In case a string is less than 2 letters, it returns an empty string.

  return string made of the first and last two letters of the original string or an empty string if the string is less than 2 letters.
  
  """
      
  
  def fixStart(self):
    char = self.string[0]
    self.string = self.string.replace(char, '*')
    self.string = char + self.string[1:]
    return self.string
  """
  This function changes letters in a string with '*' if letters are the same letter with the first letter.
  
  return string in which letters same with the first letter are replaced with '*'
  """
  #def asciiSum(self):

  #def cipher(self):


   
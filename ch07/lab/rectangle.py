class Rectangle:
  def __init__(self, x, y, height, width):
    self.x = int(x)
    self.y = int(y)
    self.height = int(height)
    self.width = int(width)
    
    if self.x < 0:
      self.x = 0
    if self.y < 0:
      self.y = 0
    if self.height < 0:
      self.height = 0
    if self.width < 0:
      self.width = 0
    
  def __str__(self):

    str = x,y,height,width

    return str



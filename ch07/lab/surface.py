import rectangle




class Surface:
  def __init__(self, filename,x, y, height, width):
    self.rect = rectangle.Rectangle(x,y,height,width)
    self.image = filename
    self.x = int(x)
    self.y = int(y)
    self.height = int(height)
    self.width = int(width)
  def getRect(self):

    return self.rect
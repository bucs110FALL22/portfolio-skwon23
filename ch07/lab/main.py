import rectangle
import surface

r = rectangle.Rectangle(10, 10, 10, 10)
assert ((r.x, r.y, r.height, r.width) == (10,10,10,10))
r = rectangle.Rectangle(-1, 1, 1, 1)
assert((r.x, r.y, r.height, r.width) == (0,1,1,1))
r = rectangle.Rectangle(1, -1, 1, 1)
assert((r.x, r.y, r.height, r.width) == (1,0,1,1))
r = rectangle.Rectangle(1, 1, -1, 1)
assert((r.x, r.y, r.height, r.width) == (1,1,0,1))
r = rectangle.Rectangle(1, 1, 1, -1)
assert((r.x, r.y, r.height, r.width) == (1,1,1,0))


s = surface.Surface("myimage.png", 10, 10, 10, 10)
assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))
s.rect = s.getRect()
assert((s.rect.x,  s.getRect().y, s.rect.height,  s.rect.width) == (10,10,10,10))
assert s.image 
print("Test Complete!")






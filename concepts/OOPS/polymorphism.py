# Polymorphism : ability of an object to perform different operations based on the object it is operating on

from multipledispatch import dispatch

class Foo:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  @dispatch(int, int)
  def xy_add(self, x, y):
    print("performing integer addition")
    return x + y
  
  @dispatch(float, float)
  def xy_add(self, x, y):
    print("performing float addition")
    return x + y

  def __add__(self, other):
    return self.x + other.x, self.y + other.y

f = Foo(12, 34)
print(f.xy_add(f.x, f.y))

f1 = Foo(1.4, 3.4)
print(f1.xy_add(f1.x, f1.y))

print(f + f1)
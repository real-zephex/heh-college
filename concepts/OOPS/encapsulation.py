# Encapsulation : bundling of attributes and methods into single unit class 

class Foo:
  def __init__(self, x, y, z):
    self.x = x
    self._y = x
    self.__z = z
  
  def display(self):
    print(self.x)
    print(self._y)
    print(self.__z)

f = Foo(1, 2, 3)
print(f.x, f._y) # the variable z is not accessible from outside as it is a private attribute of the Foo class.

f.display() # Here the value of z is also printed as the display method is part of the Foo class itself.

# Abstraction
# Concept of hiding implementation details and showing only the essential features of the object

from abc import ABC, abstractmethod

class Foo:
  def __init__(self, x):
    self.x = x

  @abstractmethod
  def bar(self):
    return self.x**2

class Foobar(Foo):
  def __init__(self, x):
    super().__init__(x)

  def bar(self):
    return self.x ** 3

f = Foobar(2)
print(f.bar())

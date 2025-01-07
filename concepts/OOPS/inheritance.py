# Inheritance : derived class inheriting attributes and methods from the base class

class Foo:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name)
    print(self.age)

class Foobar(Foo): # this is an example of single inheritance
  def __init__(self, name, age):
    super().__init__(name, age)

  def __str__(self):
    return f"Your name is {self.name} and you are {self.age} years old."

class FooFoo(Foobar, Foo): # now this is multiple inheritance - a derived class inheriting from multiple base classes
  def __init__(self, name, age):
    super().__init__(name, age)

f = Foobar("Sumit", 18)
f.display()

f1 = FooFoo("Sumit", 18)
print(f1)
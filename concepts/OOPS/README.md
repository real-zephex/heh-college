## Object-Oriented Programming (OOP) Concepts

### Abstraction
Abstraction is the concept of hiding the implementation details and showing only the essential features of the object. It helps in reducing programming complexity and effort. In Python, abstraction can be achieved using abstract classes and methods provided by the `abc` module.

#### Example:
```python
from abc import ABC, abstractmethod

class Foo(ABC):
  def __init__(self, x):
    self.x = x

  @abstractmethod
  def bar(self):
    pass

class Foobar(Foo):
  def __init__(self, x):
    super().__init__(x)

  def bar(self):
    return self.x ** 3

f = Foobar(2)
print(f.bar())  # Output: 8
```

### Encapsulation
Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, known as a class. It restricts direct access to some of the object's components, which can prevent the accidental modification of data. In Python, encapsulation can be achieved by using private and protected access modifiers.

#### Example:
```python
class Foo:
  def __init__(self, x, y, z):
    self.x = x
    self._y = y
    self.__z = z
  
  def display(self):
    print(self.x)
    print(self._y)
    print(self.__z)

f = Foo(1, 2, 3)
print(f.x, f._y)  # Output: 1 2
# print(f.__z)  # This will raise an AttributeError
f.display()  # Output: 1 2 3
```

### Inheritance
Inheritance is a mechanism where a new class (derived class) inherits attributes and methods from an existing class (base class). It promotes code reusability and establishes a relationship between different classes. Python supports single inheritance, multiple inheritance, and multilevel inheritance.

#### Example:
```python
class Foo:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name)
    print(self.age)

class Foobar(Foo):  # Single inheritance
  def __init__(self, name, age):
    super().__init__(name, age)

  def __str__(self):
    return f"Your name is {self.name} and you are {self.age} years old."

class FooFoo(Foobar, Foo):  # Multiple inheritance
  def __init__(self, name, age):
    super().__init__(name, age)

f = Foobar("Sumit", 18)
f.display()  # Output: Sumit 18

f1 = FooFoo("Sumit", 18)
print(f1)  # Output: Your name is Sumit and you are 18 years old.
```

### Polymorphism
Polymorphism is the ability of an object to perform different operations based on the object it is operating on. It allows methods to do different things based on the object it is acting upon. In Python, polymorphism can be achieved through method overloading and method overriding.

#### Example:
```python
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
print(f.xy_add(f.x, f.y))  # Output: performing integer addition 46

f1 = Foo(1.4, 3.4)
print(f1.xy_add(f1.x, f1.y))  # Output: performing float addition 4.8

print(f + f1)  # Output: (13.4, 37.4)
```
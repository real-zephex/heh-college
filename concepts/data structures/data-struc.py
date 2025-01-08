# Data Structures
# Fundamental components in computer science that defines how data is organized, stored, and manipulated within a program.

"""
There are 2 types of data structures:
  1. Primitive data structures
  2. Abstract data structures
"""

"""
1. Primitive Data Structures
Basic types of data structures that directly operate on machine instructions. They are fundamental to building more complex data structures and are provided as built-in types in a programming language.
E.g.: int, str, float, bool, etc.

2. Abstract Data Structures
More complex data structures that are built using primitive data structures. Provide a way to organize and store data in a manner that allows for efficient access and modification.
E.g.: list, stacks, queues, etc.
"""

class Stacks:
  """
    Collection that follows Last In First Out (LIFO) principle. 

    Key operations:
      1. push
      2. pop
      3. peek
      4. isEmpty
  """

  def __init__(self, args: list):
    self.args = args

  def pop(self) -> None: 
    self.args.pop()

  def push(self, el) -> None:
    self.args.append(el)
  
  def peek(self):
    return self.args[0]

  def isEmpty(self) -> bool:
    return len(self.args) == 0;

  def __str__(self):
    return ", ".join(str(i) for i in self.args)

s = Stacks([1, 2, 3, 4, 5])
s.pop()
print(s)

s.push(4)
print(s)

print(s.peek())

print(s.isEmpty())

class Queue:
  """
    Collection that follows the First In First Out principle (FIFO)

    Key operations:
      1. enqueue : add an element at the back of the queue
      2. dequeue : remove and return the front element of the queue
      3. front : return the front element without removing it
      4. isEmpty : check if the queue is empty or not
  """

  def __init__(self, args: list):
    self.args = args

  def enqueue(self, el):
    self.args.append(el)

  def dequeue(self):
    return self.args.pop(0)

  def front(self):
    return self.args[0]

  def isEmpty(self):
    return len(self.args) == 0
  
q = Queue([1, 2, 3, 4, 5])
print(q.args)

# Dequeue
print(q.dequeue())
print(q.args)

# Enqueue
q.enqueue(4)
print(q.args)

print(q.front())

print(q.isEmpty())
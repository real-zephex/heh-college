# *args - pass multiple arguments to a function without actually defining parameters for each arguments (returns a tuple)

def func(*args) -> tuple:
  return args

print(func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# *kwargs - pass multiple key-value pairs to a function without having to assign new parameter for each entry (returns a dictionary)

def foo(**kwargs) -> dict:
  return kwargs

print(foo(message="Hello World", number = 100)) 
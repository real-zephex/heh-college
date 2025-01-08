# List Comprehension
# It is a concise way to create lists in Python. It allows for generation of a new list by applying an expression to each item of an existing iterable.
# Syntax: [expression for item in iterable if condition]

# Program to generate a list of numbers upto 50
number_upto_50 = [i for i in range(1, 51)]
print(number_upto_50)

# Even numbers upto 50
even_numbers = [i for i in number_upto_50 if i % 2 == 0]
print(even_numbers)

# Odd Numbers
odd_numbers = [i for i in number_upto_50 if i not in even_numbers]
print(odd_numbers)

# Prime Numbers upto 50
def prime_check(number: int) -> bool:
  isPrime = True
  if number < 2:
    return False
  for i in range(2, number):
    if number % i == 0:
      isPrime = False
      break

  return isPrime

primes = [i for i in number_upto_50 if prime_check(i)]
print(primes)
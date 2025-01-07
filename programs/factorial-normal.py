# Write a program to find the factorial of a number using the normal method

def factorial(num: int) -> int:
  product = 1
  for i in range(1, num + 1):
    product *= int(i)
  return product

user_input = int(input("Enter number: "))
print(factorial(user_input))

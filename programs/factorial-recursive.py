# Write a program to find the factorial of a given number using the recursive method

def factorial(num: int) -> int:
  if num == 1:
    return num
  else:
    return num * factorial(num - 1)

user_input = int(input("Enter number to check: "))
print(factorial(user_input))
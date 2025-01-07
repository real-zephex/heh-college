# Write a program to print the nth fibanocci number

def number_finder(num: int):
  if num == 1:
    return 0
  elif num == 2:
    return 1
  
  a, b = 0, 1

  for _ in range(2, num):
    a, b = b, a + b
  
  return b

n = int(input("Enter number: "))
print(number_finder(n))
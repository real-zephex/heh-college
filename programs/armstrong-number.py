# Write a program to check whether a number is an armstrong number or not.

def armstrong_check(num: str) -> bool:
  sumList = [int(i)**len(num) for i in num]
  return sum(sumList) == int(num)

user_input = input("Enter number to check: ")
if armstrong_check(user_input):
  print(f"{user_input} is an armstrong number.")
else:
  print(f"{user_input} is not an armstrong number.")
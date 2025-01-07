# Write a program to find all the armstrong numbers in a given range.

def armstrong_check(num: int) -> bool:
  sumList = [int(i)**len(num) for i in num]
  return sum(sumList) == int(num)

lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))

for i in range(lower_range, upper_range + 1):
  if armstrong_check(str(i)):
    print(f"Armstrong number found: {i}")
  
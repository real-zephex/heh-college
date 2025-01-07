# Write a program to print the fibanocci series upto a given range

rg = int(input("Enter number: "))

x, y = 0, 1
print(x, y, end=" ")

for _ in range(rg):
  next = x + y
  print(next, end=" ")
  x = y
  y = next
print()
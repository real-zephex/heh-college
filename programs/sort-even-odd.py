# Write a program to sort out even and odd numbers from a list of numbers

import random

num_list = []
for _ in range(50): 
  if _ not in num_list:
    num_list.append(random.randint(1, 50))

even = filter(lambda x: x % 2 == 0, num_list)
print(list(even))

odd = filter(lambda x: x % 2 != 0, num_list)
print(list(odd))
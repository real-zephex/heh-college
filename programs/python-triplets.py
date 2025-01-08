# Write a program to generate the pythagorean triples upto a given range

limit = 25

for i in range(1, int(limit ** 1/2) + 1):
  for j in range(1, i):
    a = i**2 - j**2
    b = 2 * i * j
    c = i**2 + j**2
    if c <= limit:
      print(a, b, c)

  

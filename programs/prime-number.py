# Write a program to check whether a number is prime or not
def prime_check(num: int) -> bool:

  isPrime = True
  if num < 2:
    return False
  else:
    for i in range(2, num):
      if num % i == 0:
        isPrime = False
        break

  return isPrime

num = int(input("Enter number: "))
if prime_check(num):
  print(f"{num} is a prime number.")
else:
  print(f"{num} is not a prime number.")

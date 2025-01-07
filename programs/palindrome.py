# Write a program to check whether the given string is a palindrome or not.

def palindrome_check(string: str) -> bool:
  stringList = [i for i in string]
  return stringList == stringList[::-1]

user_input = input("Enter the string to check: ")
if palindrome_check(user_input):
  print("The given string is a palindrome.")
else:
  print("The given string is not a palindrome")
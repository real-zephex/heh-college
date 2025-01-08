# Write a program which takes in a string as an input, reverses it and returns it

def reverse_string(string: str):
  return string[::-1]

user_input = input("Enter string: ")
print(reverse_string(user_input))
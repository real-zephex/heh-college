# Problems related to regex
import re

"""
Write a program to match any string that contains the word Python in it.
"""

def question(string: str):
  pattern = r"PYTHON"
  match = re.findall(pattern, string, re.IGNORECASE) 
  return match


"""
Write a program to match phone numbers (10 digits) from a string
""" 

def question_two(string: str):
  pattern = r"\d{10}"
  match = re.findall(pattern, string)
  return match

user_input = input("Enter string you want to check: ")
print(question_two(user_input))

"""

"""
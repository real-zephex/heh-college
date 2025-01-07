# Write a program to classify person as child, teenager, adult, or senior based on the following criterias.

"""
  Child : age < 12
  Teenager : 12 <= age <= 17
  Adult : 18 <= age <= 59
  Senior : age >= 60
"""

def classify_age(age: int) -> str:
  if age < 12:
    return "Child"
  elif 12 <= age <= 17:
    return "Teenager"
  elif 18 <= age <= 59:
    return "Adult"
  else:
    return "Senior"

age = int(input("Enter the age: "))
classification = classify_age(age)
print(f"The person is classified as: {classification}")
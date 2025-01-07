# Write a program which asks user for their marks and then calculate their percentage. The program should also assign grades to the students based on their percentage score.

'''
  A : marks >= 90
  B : 80 <= marks <= 89
  C : 70 <= marks <= 79
  D : 60 <= marks <= 69
  E : marks < 60
'''

def assign_marks(score: int) -> str:
  if score >= 90:
    return "A"
  elif score <= 89 and score >= 80:
    return "B"
  elif score <= 79 and score >= 70:
    return "C"
  elif score <= 69 and score >= 60:
    return "D"
  else:
    return "E"

def main():
  total_marks = int(input("Enter the total marks: "))
  obtained_marks = int(input("Enter the obtained marks: "))
  
  if total_marks <= 0:
    print("Total marks should be greater than zero.")
    return
  
  percentage = (obtained_marks / total_marks) * 100
  grade = assign_marks(percentage)
  
  print(f"Percentage: {percentage:.2f}%")
  print(f"Grade: {grade}")

main()
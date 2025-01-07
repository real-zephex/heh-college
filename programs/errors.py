"""
  Program to showcase handling of a Zero Division Error using exception handling.
"""
def divide_numbers(a, b):
  try:
    result = a / b
  except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
  else:
    print(f"The result is {result}")
  finally:
    print("Execution of the division operation is complete.")

divide_numbers(10, 2)
divide_numbers(10, 0)


"""
  Program to handle multiple errors.
"""
def calculate_value(a, b):
    try:
        result = int(a) / int(b)
        return result
    except ValueError:
        print("Error: Please enter valid numbers")
    except ZeroDivisionError:
        print("Error: Division by zero not allowed")
    except Exception as e:
        print(f"Unexpected error: {e}")

num_a = input("Enter number 1: ")
num_b = input("Enter number 2: ")

calculate_value(num_a, num_b)


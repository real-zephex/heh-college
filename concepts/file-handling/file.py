# File Handling : Allows the program to read from and write to files.

def write():
  user_input = input("Enter message: ")
  with open("file.txt", "w") as file:
    file.write(user_input)

def read():
  with open("file.txt", "r") as file:
    content = file.readlines() # Reads the entire file as a single string
    #         file.readlines() # Reads the entire file at once but breaks into list at each new line character
    #         file.readline() # Reads the file line by line

    print(content)

read()
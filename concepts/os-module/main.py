# OS Module
"""
  Here, we will be perfoming a very simple task
    1. Print the current working directory
    2. Create a new directory and chdir into it
    3. Create a new directory inside this directory and then rename it to something else.
    4. Delete this directory 
"""

import os

def getcwd():
  print(os.getcwd())

getcwd()

os.mkdir("test-folder")
print(os.listdir())

os.chdir("test-folder")
getcwd()

os.mkdir("folder-2")
print(os.listdir())

os.rename("folder-2", "haha")
print(os.listdir())

os.rmdir("haha")
os.chdir("..")

os.rmdir("test-folder")

getcwd()
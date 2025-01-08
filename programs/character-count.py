# Write a program which counts the occurence of each letter of a word and stores it in a dictionary

def main(word: str):
  word_dict = {
    i: word.count(i) for i in set(word)
  }
  return word_dict

user_input = input("Enter word: ")
print(main(user_input))
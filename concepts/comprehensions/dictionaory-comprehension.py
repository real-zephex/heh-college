# Dictionary Comprehension
# Dictionary comprehension is a concise and efficient way to create dictionaries in Python. It allows for the generation of a new dictionary by applying an expression to each item in an existing iterable.
# Syntax: {key_expression: value_expression for item in iterable if condition}

# Create a dictionary of odd and even numbers
numbers = range(50)

even_odd ={
  "even": [i for i in numbers if i % 2 == 0],
  "odd": [i for i in numbers if i % 2 != 0]
}
print(even_odd)

# Create a dicitonary which has numbers as its key values and the squares of those numbers as the values
squares = {
  i: i**3 for i in range(1, 11)
}
print(squares)

# Use the zip method
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
merged_dict = {k: v for k, v in zip(keys, values)}
print(merged_dict)

# Count the occurance of each letter in a string 
text = "dictionary comprehension"
char_count = {char: text.count(char) for char in set(text)}
print(char_count)

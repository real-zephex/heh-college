# Comprehensions in Python

Comprehensions provide a concise way to create lists, dictionaries, and other collections in Python. They allow for the generation of a new collection by applying an expression to each item in an existing iterable.

## List Comprehension

List comprehension is a concise way to create lists. It allows for the generation of a new list by applying an expression to each item of an existing iterable.

### Syntax
```python
[expression for item in iterable if condition]
```

### Example
```python
# Generate a list of numbers up to 50
number_upto_50 = [i for i in range(1, 51)]

# Generate a list of even numbers up to 50
even_numbers = [i for i in number_upto_50 if i % 2 == 0]
```

## Dictionary Comprehension

Dictionary comprehension is a concise and efficient way to create dictionaries. It allows for the generation of a new dictionary by applying an expression to each item in an existing iterable.

### Syntax
```python
{key_expression: value_expression for item in iterable if condition}
```

### Example
```python
# Create a dictionary of numbers and their squares
squares = {i: i**2 for i in range(1, 11)}

# Create a dictionary from two lists using zip
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
merged_dict = {k: v for k, v in zip(keys, values)}
```

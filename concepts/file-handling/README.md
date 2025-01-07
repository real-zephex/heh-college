# File Handling in Python

File handling is an essential part of any programming language. Python provides several functions for creating, reading, updating, and deleting files.

## Opening a File

To open a file in Python, use the `open()` function. The `open()` function takes two parameters: filename and mode.

```python
file = open('example.txt', 'r')  # Open file for reading
```

### Modes

- `'r'` - Read mode (default). Opens a file for reading.
- `'w'` - Write mode. Opens a file for writing (creates a new file or truncates an existing file).
- `'a'` - Append mode. Opens a file for appending (creates a new file if it does not exist).
- `'b'` - Binary mode. Opens a file in binary mode.
- `'t'` - Text mode (default). Opens a file in text mode.
- `'x'` - Exclusive creation mode. Creates a new file and fails if the file already exists.

## Reading a File

To read a file's content, you can use several methods:

- `read()`: Reads the entire file.
- `readline()`: Reads a single line from the file.
- `readlines()`: Reads all lines into a list.

```python
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
```

## Writing to a File

To write to a file, use the `write()` or `writelines()` methods.

```python
file = open('example.txt', 'w')
file.write('Hello, World!')
file.close()
```

## Appending to a File

To append content to an existing file, use the append mode `'a'`.

```python
file = open('example.txt', 'a')
file.write('\nAppending a new line.')
file.close()
```

## Closing a File

Always close a file after completing operations to free up system resources.

```python
file.close()
```

## Using `with` Statement

Using the `with` statement is a better practice as it ensures the file is properly closed after its suite finishes.

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

## File Methods

- `file.read(size)`: Reads `size` bytes from the file.
- `file.readline(size)`: Reads a line with a maximum of `size` bytes.
- `file.readlines()`: Reads all lines and returns them as a list.
- `file.write(string)`: Writes a string to the file.
- `file.writelines(list)`: Writes a list of strings to the file.
- `file.close()`: Closes the file.

## File Handling Exceptions

Handle exceptions using `try` and `except` blocks to manage errors during file operations.

```python
try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print('File not found.')
finally:
    file.close()
```

## Summary

File handling in Python is straightforward with the `open()` function and various file methods. Always ensure to close files or use the `with` statement for better resource management.

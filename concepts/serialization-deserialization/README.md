# Python Serialization and Deserialization

This guide covers two main methods of serialization in Python: Pickle and JSON.

## What is Serialization?

Serialization is the process of converting data structures or object state into a format that can be stored or transmitted and reconstructed later.

## Pickle Module

### Advantages

- Can serialize almost any Python object
- Maintains object references
- Python-specific optimization

### Disadvantages

- Not secure for untrusted data
- Python-specific (not cross-language compatible)
- Binary format (not human-readable)

```python
import pickle

# Serialization
pickle.dump(data, file_object)
pickle.dumps(data)  # Returns bytes

# Deserialization
data = pickle.load(file_object)
data = pickle.loads(bytes_object)
```

## JSON Module

### Advantages

- Human-readable format
- Language-independent
- Widely supported
- Secure for data exchange

### Disadvantages

- Limited to basic data types
- No support for complex Python objects
- No circular reference support

```python
import json

# Serialization
json.dump(data, file_object)
json.dumps(data)  # Returns string

# Deserialization
data = json.load(file_object)
data = json.loads(string)
```

## When to Use Which?

- Use **Pickle** when:

  - Serializing Python-specific objects
  - Working within Python ecosystem
  - Need to preserve object references

- Use **JSON** when:
  - Interoperating with other languages/systems
  - Need human-readable format
  - Working with web APIs
  - Security is a concern

## But where ot use JSON and where to use pickle?

Well, `json` format is mainly used when dealing with web apis as the information needs to be in human readabale format. But when the data needs to be transferred over the network the pickle module is used the binary format is preferred for transmitting data.

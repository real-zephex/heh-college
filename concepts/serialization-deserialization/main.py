"""
Serialization and Deserialization in Python

1. Pickle Module:
   - Used for serializing Python objects to binary format
   - Can handle complex Python objects
   - Not secure for untrusted data
   - Python-specific (not cross-language compatible)

2. JSON Module:
   - Used for serializing data to JSON format
   - Human-readable format
   - Cross-language compatible
   - Limited to basic data types
"""

import pickle
import json

# Sample data
data_to_serialize = {
    "message": "hello world",
    "time": 1752,
    "list": [1, 2, 3],
    "dict": {"a": 1, "b": 2}
}

# -------- Pickle Serialization --------
# Writing to binary file
with open("file.pkl", "wb") as file:
    pickle.dump(data_to_serialize, file)

# Pickle Deserialization
with open("file.pkl", "rb") as file:
    pickle_data = pickle.load(file)
print("Pickle deserialized data:", pickle_data)

# -------- JSON Serialization --------
# Writing to JSON file
with open("file.json", "w") as file:
    json.dump(data_to_serialize, file, indent=4)

# JSON string serialization
json_string = json.dumps(data_to_serialize)
print("\nJSON string:", json_string)

# JSON Deserialization
with open("file.json", "r") as file:
    json_data = json.load(file)
print("\nJSON deserialized data:", json_data)

# JSON string deserialization
decoded_json = json.loads(json_string)
print("\nDecoded JSON string:", decoded_json)
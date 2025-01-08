# Serialization and deserializaiton using json module

import json

object_to_be_written = {
  "message": "hello world",
  "number": 233
}

# Writing to the JSON file
with open("file.json" , "w") as file:
  json.dump(object_to_be_written, file)

# Reading from the JSON file
with open("file.json", "r") as file:
  data = json.load(file)
  print(data)



# Write a function to read a JSON file and return it as a Python dictionary.
import json

def read_json(file_name):
    with open(file_name, mode = 'r') as file:
        return json.load(file)
    
print(read_json("output.json"))

        
import json

with open("Python\\data\\json.json") as data:
    json_reader = data.read()
    print(json_reader)

json_python = json.load(json_reader)
print(json_python)

"""
with open("json_sample.json", "w") as fh:
    json.dumps(json_reader, fh, indent = 4)
    
"""
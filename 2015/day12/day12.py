import re
import json

doc = open("input").read()
part1 = sum(int(n) for n in re.findall(r'-?\d+', doc))

def count(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(count(item) for item in obj)
    elif isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        else:
            return sum(count(val) for val in obj.values())
    else:
        return 0

data = json.loads(doc)
part2 = count(data)

print(part1, part2)

import json
import os
import random

with open(os.path.join(os.path.dirname(__file__),
                       './txzips.json')) as zips_file:
    zips = json.load(zips_file)

data = {"zipweights": []}
i = 0
for zipObj in list(zips["texaszips"]):
    weight = int(zips["texaszips"][zipObj]["population"])
    if i > 0:
        weight = weight + data["zipweights"][i - 1]
    data["zipweights"].append(weight)
    i = i + 1

with open("cumuweights.json", 'w') as f:
    json.dump(data, f, indent=4)

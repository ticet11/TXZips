import os
import json

with open(os.path.join(os.path.dirname(__file__), './tx.json')) as zip_file:
    zipObjs = json.load(zip_file)
    data = []
    count = 0
    for zipObj in zipObjs:
        count += 1
        if zipObjs[zipObj]['city'] not in data:
            data.append(zipObjs[zipObj]['city'])
    print(count)
    print(len(data))

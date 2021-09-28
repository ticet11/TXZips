import json

with open('../data/tx.json') as zip_file:
    zipObjs = json.load(zip_file)
    data = []
    count = 0
    for zipObj in zipObjs:
        count += 1
        if zipObjs[zipObj]['city'] not in data:
            data.append(zipObjs[zipObj]['city'])
    print(f'Unique ZipCodes: {count}')
    print(f'Unique Cities: {len(data)}')

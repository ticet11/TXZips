import json
import random

with open('../data/txzips.json') as zips_file:
    zips = json.load(zips_file)

zipKey = random.choice(list(zips["texaszips"]))
zipObj = zips["texaszips"][zipKey]

userLocation = {
    'userCity': zipObj["city"],
    'userCounty': zipObj["countyname"],
    'userState': 'Texas',
    'userZip': zipKey,
}

print(userLocation)

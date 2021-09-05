import json
import os
import random

with open(os.path.join(os.path.dirname(__file__), './txzips.json')) as zips_file:
    zips = json.load(zips_file)

zipKey = random.choice(list(zips["texaszips"]))
zipObj = zips["texaszips"][zipKey]

userLocation = {
    'userCity': zipObj["city"],
    'userCounty': zipObj["countyname"],
    'userState': zipObj["statename"] if random.choice([True, False]) else zipObj["stateid"],
    'userZip': zipKey,
}

print(userLocation)

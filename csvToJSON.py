import json
import csv

with open("uszips.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"texaszips": {}}
    for row in reader:
        if row[4] == 'TX':
            data["texaszips"][row[0]] = {
                "latitude": row[1],
                "longitude": row[2],
                "city": row[3],
                "stateid": row[4],
                "statename": row[5],
                "zcta": row[6],
                "parent_zcta": row[7],
                "population": row[8],
                "density": row[9],
                "countyfips": row[10],
                "countyname": row[11],
                "countyweights": row[12],
                "countynamesall": row[13],
                "countyfipsall": row[14],
                "imprecise": row[15],
                "military": row[16],
                "timezone": row[17],
            }


with open("txzips.json", 'w') as f:
    json.dump(data, f, indent=4)

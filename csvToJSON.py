import json
import csv
import os

with open(os.path.join(os.path.dirname(__file__),
                       './ip_addresses.json')) as ip_file:
    cities = json.load(ip_file)
    with open(os.path.join(os.path.dirname(__file__),
                           './txzips.json')) as zip_file:
        zips = json.load(zip_file)
        data = {"state": ["TX", "Texas"], "cities": {}}
        for key in cities["TX"]:
            data["cities"][key] = {
                "ip_addresses": cities["TX"][key],
                "zip_codes": []
            }

            for zipKey in zips["zip_codes"]:
                if zipKey["city"] == key:
                    data["cities"][key]["zip_codes"].append({
                        "zip":
                        zipKey["zip"],
                        "countyname":
                        zipKey["countyname"],
                        "pop":
                        zipKey["pop"],
                    })

with open("tx.json", 'w') as f:
    json.dump(data, f, indent=4)

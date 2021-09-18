import json
import csv
import os

with open("IP2LOCATION-LITE-DB9.CSV") as f:

    def long2DotIP(ipnum):
        return str(int(ipnum / 16777216) % 256) + "." + str(
            int(ipnum / 65536) % 256) + "." + str(
                int(ipnum / 256) % 256) + "." + str(ipnum % 256)

    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        if row[4] == 'Texas':
            data.append({
                "ip_address_range": {
                    "low": long2DotIP(int(row[0])),
                    "high": long2DotIP(int(row[1])),
                },
                "city": row[5],
                "zip": row[8]
            })

with open("tx_ip_by_zip.json", 'w') as f:
    json.dump(data, f, indent=4)

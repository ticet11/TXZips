import json
import csv
import ipaddress

with open("../data/IP2LOCATION-LITE-DB9.CSV") as csvData:

    reader = csv.reader(csvData)
    next(reader)  # skip title lines
    data = {}
    for row in reader:
        if row[4] == 'Texas':
            formattedIpRanges = []
            rowIpRanges = [
                ipaddr for ipaddr in ipaddress.summarize_address_range(
                    ipaddress.IPv4Address(int(row[0])),
                    ipaddress.IPv4Address(int(row[1])))
            ]
            for rowIpRange in rowIpRanges:
                formattedIpRanges.append(format(rowIpRange))

            data[row[8]] = {
                "ip_address_range": formattedIpRanges,
            }

with open("../data/tx_ip_by_zip.json", 'w') as f:
    json.dump(data, f, indent=4)

    # with open("../data/uszips.csv", "r") as uszips:
    #     reader = csv.reader(uszips)
    #     next(reader)
    #     data = {"texaszips": {}}
    #     for row in reader:
    #         if row[4] == 'TX':
    #             data["texaszips"][row[0]] = {
    #                 "latitude": row[1],
    #                 "longitude": row[2],
    #                 "city": row[3],
    #                 "stateid": row[4],
    #                 "statename": row[5],
    #                 "zcta": row[6],
    #                 "parent_zcta": row[7],
    #                 "population": row[8],
    #                 "density": row[9],
    #                 "countyfips": row[10],
    #                 "countyname": row[11],
    #                 "countyweights": row[12],
    #                 "countynamesall": row[13],
    #                 "countyfipsall": row[14],
    #                 "imprecise": row[15],
    #                 "military": row[16],
    #                 "timezone": row[17],
    #             }

    # def long2DotIP(ipnum): # Convert ip number to dot notation
    #     return str(int(ipnum / 16777216) % 256) + "." + str(
    #         int(ipnum / 65536) % 256) + "." + str(
    #             int(ipnum / 256) % 256) + "." + str(ipnum % 256)

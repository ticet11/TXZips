import json
import csv
import os
import ipaddress

with open("IP2LOCATION-LITE-DB9.CSV") as f:

    def long2DotIP(ipnum):
        return str(int(ipnum / 16777216) % 256) + "." + str(
            int(ipnum / 65536) % 256) + "." + str(
                int(ipnum / 256) % 256) + "." + str(ipnum % 256)

    reader = csv.reader(f)
    next(reader)
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

    #     if row[4] == 'Texas' and row[5] == 'Abilene':
    #         rowIpRanges = [
    #             ipaddr for ipaddr in ipaddress.summarize_address_range(
    #                 ipaddress.IPv4Address(int(row[0])),
    #                 ipaddress.IPv4Address(int(row[1])))
    #         ]
    #         for rowIpRange in rowIpRanges:
    #             ipRanges.append(format(rowIpRange))
    # print(ipRanges)

with open("tx_ip_by_zip.json", 'w') as f:
    json.dump(data, f, indent=4)

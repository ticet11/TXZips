import ipaddress

formattedIpRanges = []


def ipRangeFormatter(low, high):
    rowIpRanges = [
        ipaddr for ipaddr in ipaddress.summarize_address_range(
            ipaddress.IPv4Address(low), ipaddress.IPv4Address(high))
    ]
    for rowIpRange in rowIpRanges:
        formattedIpRanges.append(format(rowIpRange))


ipRangeFormatter('34.9.77.0', '34.131.205.255')
ipRangeFormatter('34.131.207.0', '34.191.255.255')
ipRangeFormatter('16.35.199.0', '16.73.223.255')
ipRangeFormatter('16.186.156.0', '16.213.252.255')
ipRangeFormatter('16.160.30.0', '16.186.154.255')

print(formattedIpRanges)

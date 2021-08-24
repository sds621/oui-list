# Created by Sasha Sashington
#!/usr/bin/env python
''' This program with read in a list of mac addresses and create a new list containing
only the manufacturer identification portion of the mac address, excluding duplicates
and print the new list to a text file.
'''

from __future__ import print_function, unicode_literals, division
from pprint import pprint

vendor_list = []

# Open file and read contents
with open("unknown-macs.txt") as f:
    unknown_macs = f.read()
unknown_macs = unknown_macs.splitlines()

# Obtain fist 3 octects of the mac address and append it to vendor_list, excluding duplicates
for mac_addr in unknown_macs:
    mac_addr = mac_addr.split(":")
    mac_addr = mac_addr[:3]
    mac_addr = ":".join(mac_addr)
    if mac_addr not in vendor_list:
        vendor_list.append(mac_addr)

# Print results to file
vendor_str = '\n'.join(map(str,vendor_list))
with open("vendor_list.txt", 'w') as output:
    output.write(str(vendor_str))

#!/bin/env python3

import subprocess
import optparse
import re


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


option = get_argument()
ifconfig_result = subprocess.check_output(["ifconfig", option.interface])
octet = "[0-9a-fA-F][0-9a-fA-F]"
rule = '{}:{}:{}:{}:{}:{}'.format(octet, octet, octet, octet, octet, octet)
print(rule)
rrule = re.compile(rule)
mac_address_search_result = re.search(rrule, ifconfig_result)
# print(rule)
# change_mac(option.interface, option.new_mac)

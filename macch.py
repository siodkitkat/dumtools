#!/usr/bin/env python

import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interf", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_m", help="New MAC acddr")
    (options , arguments) = parser.parse_args()
    if not options.interf:
        parser.error(" - please specify interface or use --help")
    elif not options.new_m:
        parser.error(" - please specify MAC or use --help")
    return options

def change_mac(interf, new_m):
    print(" + Changing MAC address for " + interf + " to " + new_m)
    subprocess.call(["ifconfig", interf , "down"])
    subprocess.call(["ifconfig", interf , "hw", "ether", new_m])
    subprocess.call(["ifconfig", interf , "up"])


options = get_args()
change_mac(options.interf , options.new_m)



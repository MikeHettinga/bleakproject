#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import os
import subprocess


### HELPER FUNCTIONS (IF NECESSARY) ###
def advrecon(target):

    if not os.path.exists(str(target)):
        os.makedirs(str(target))
    print("Starting DNSRecon Scan")
    subprocess.call("dnsrecon -d " + str(target) + " -a > " + str(target) + "/" + target + "_dnsoutput", shell=True)
    print("DNSRecon Scan Complete")
    print("Starting Wafw00f scan")
    subprocess.call("wafw00f " + "http://" + str(target) + " > " + str(target) + "/" + target + "_wafw00f", shell=True)
    print("Wafw00f Scan Complete")
    print("Starting CMSeek Scan. If command prompt not automatically returned after 10 seconds, press Enter")
    subprocess.call("cmseek -u " + "http://" + str(target) + " > " + str(target) + "/" + target + "_cmseek", shell=True)
    print("CMSeek Scan Complete")
    print("Advanced Recon Scan Complete. See " + target + " directory for output files")


### MAIN FUNCTION ###
def main():
    target = sys.argv[1]
    advrecon(target)






### DUNDER CHECK ###
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import os
import subprocess


### HELPER FUNCTIONS (IF NECESSARY) ###
def advrecon(target):

    if not os.path.exists(str(target)):
        os.makedirs(str(target))
    # subprocess.call("dnsrecon -d " + str(target) + " -a > " + target + "_dnsoutput", shell=True)
    # # target = "http://" + target
    # subprocess.call("wafw00f " + "http://" + str(target) + " > "  + target + "_wafw00f", shell=True)
    # subprocess.call("cmseek -u " + "http://" + str(target) + " > "  + target + "_cmseek", shell=True)
    print("Starting DNSRecon Scan")
    subprocess.call("dnsrecon -d " + str(target) + " -a > " + str(target) + "/" + target + "_dnsoutput", shell=True)
    print("DNSRecon Scan Complete")
    # target = "http://" + target
    print("Starting Wafw00f scan")
    subprocess.call("wafw00f " + "http://" + str(target) + " > " + str(target) + "/" + target + "_wafw00f", shell=True)
    print("Wafw00f Scan Complete")
    print("Starting CMSeek Scan. If command prompt not automatically returned after 10 seconds, press Enter")
    subprocess.call("cmseek -u " + "http://" + str(target) + " > " + str(target) + "/" + target + "_cmseek", shell=True)
    print("CMSeek Scan Complete")
    print("Advanced Recon Scan Complete. See " + target + " directory for output files")


### MAIN FUNCTION ###
def main():
    #declare variable called target and set it to the first argument
    target = sys.argv[1]
    # target = "zonetransfer.me"
    advrecon(target)






### DUNDER CHECK ###
if __name__ == "__main__":
    main()

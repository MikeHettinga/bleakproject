#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import os
import subprocess


### HELPER FUNCTIONS (IF NECESSARY) ###
def advrecon(target):

    if not os.path.exists(str(target)):
        os.makedirs(str(target))
    subprocess.call("dnsrecon -d " + str(target) + " -a", shell=True)
    subprocess.call("wafw00f " + "http://" + str(target), shell=True)
    subprocess.call("cmseek -u " + "http://" + str(target), shell=True)
    subprocess.call("dnsrecon -d " + str(target) + " -a > " + str(target) + "/" + target + "_dnsoutput", shell=True)
    subprocess.call("wafw00f " + "http://" + str(target) + " > " + str(target) + "/" + target + "_wafw00f", shell=True)
    subprocess.call("cmseek -u " + "http://" + str(target) + " > " + str(target) + "/" + target + "_cmseek", shell=True)
    print("Complete. See " + target + " directory for output files")


### MAIN FUNCTION ###
def main():
    #declare variable called target and set it to the first argument
    target = sys.argv[1]
    advrecon(target)






### DUNDER CHECK ###
if __name__ == "__main__":
    main()

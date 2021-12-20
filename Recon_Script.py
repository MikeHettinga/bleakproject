#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import os
import subprocess


### HELPER FUNCTIONS (IF NECESSARY) ###
def advrecon(target):
    # import dnsrecon_sript
    # import wafw00f_script
    # import cmseek_script

    # subprocess.call("dnsrecon -d" + str(target) + "-a >" + str(target) + "_dnsrecon_output", shell=True)
    # subprocess.call("wafw00f -a" + str(target) + ">" + str(target) + "_wafw00f_output", shell=True)
    subprocess.call("dnsrecon -d " + str(target) + " -a", shell=True)
    target = "http://" + target
    subprocess.call("wafw00f " + str(target), shell=True)
    subprocess.call("cmseek -u " + str(target), shell=True)
        # if input()!= "y":
        #     input() =


### MAIN FUNCTION ###
def main():
    #declare variable called target and set it to the first argument
    target = sys.argv[1]
    # target = "zonetransfer.me"
    advrecon(target)






### DUNDER CHECK ###
if __name__ == "__main__":
    main()

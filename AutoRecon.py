#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import os
import subprocess



### HELPER FUNCTIONS (IF NECESSARY) ###
def advrecon(target):

    if not os.path.exists(str(target)):
        os.makedirs(str(target))
    print("-----AUTORECON SCANS STARTING-----")
    print("-----Starting DNSRecon Scan-----")
    subprocess.call("dnsrecon -d " + str(target) + " -a > " + str(target) + "/" + target + "_dnsoutput", shell=True)
    subprocess.call("./seekline_dns.py /media/sf_F_DRIVE/cybersec/python/Recon_Script/" + target + "/" + target +"_dnsoutput", shell=True)
    # print("\n")
    print("-----DNSRecon Scan Complete-----")
    # print("\n")
    print("-----Starting Wafw00f Scan-----")
    subprocess.call("wafw00f " + "http://" + str(target) + " > " + str(target) + "/" + target + "_wafw00f", shell=True)
    subprocess.call(
        "./seekline_waf.py /media/sf_F_DRIVE/cybersec/python/Recon_Script/" + target + "/" + target + "_wafw00f",
        shell=True)
    # print("\n")
    print("-----Wafw00f Scan Complete-----")
    # print("\n")
    print("-----Starting CMSeek Scan-----")
    subprocess.call("cmseek -u " + "http://" + str(target) + " --follow-redirect > " + str(target) + "/" + target + "_cmseek", shell=True)
    subprocess.call(
        "./seekline.py /media/sf_F_DRIVE/cybersec/python/Recon_Script/" + target + "/" + target + "_cmseek", shell=True)
    # print("\n")
    print("-----CMSeek Scan Complete-----")
    print("-----AUTORECON Scan Complete----- \nSee " + target + " directory for output files")


### MAIN FUNCTION ###
def main():
    target = sys.argv[1]
    advrecon(target)






### DUNDER CHECK ###
if __name__ == "__main__":
    main()

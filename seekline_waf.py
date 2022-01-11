#! /usr/bin/env python3
import sys

#Function to take open file, remove the top results (indicated by an astrix) and print results. 

def linepull(file):

    for line in file:
        line = line.rstrip()
        if "[-]" in line:
            print(line)
        elif "[+]" in line:
            print(line)
        elif "[-] Zone Transfer Failed" in line:
            print("[-] Zone Transfer Failed")
        elif "[+] Zone Transfer was successful!!" in line:
            print("[+] Zone Transfer was successful!!")





        # for char in line:
        #     # make char the search character for designating lines to pull.
        #     if char == '[*]':
        #         print(line)
        #         # could be altered using .write() to create new file if desired.
        
def main():
    
    file_name = sys.argv[1]
    with open(file_name) as file:
      linepull(file) 

if __name__ == "__main__":
    main()
    

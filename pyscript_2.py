#!/usr/bin/python



import subprocess

# The first event in pyscript_2 is to call the pyscript_3 script
import pyscript_3

# After returning from the pyscript_3.py, these next three bash commands will execute
subprocess.call("ls -la", shell=True)
subprocess.call("cat pyscript_1.py", shell=True)

# note that this bash command actually calls pyscript_3.py again
subprocess.call("python ./pyscript_3.py", shell=True)

# A function to print the word "two" will be the final event in pyscript_2.py
def pys_2(): 
	print('two')

pys_2()
#!/usr/bin/python

## the unanswered question is do the following events from all files run concurrently or sequentially.  I need to find that out.



# The first event is to call the pyscript_2.py file
import pyscript_2

#This will end up being the last event and is run after the return from pyscript_2.

print('hello')

# if __name__ == '__main__':
# 	funct()
 
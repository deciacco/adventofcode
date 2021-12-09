#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "|)ehko"     
__version__ = "0.1.0"
__license__ = "MIT"

# Load libraries
import os
import sys

# Constants
OWNP = os.path.abspath(os.path.dirname(sys.argv[0])) # Own path

def main():
    
    measurements = []
    counter = 0
    ndx = 0
    
    with open(OWNP + '/input.txt', 'r') as f:
        for line in f:
            measurements.append(int(line.rstrip('\n').rstrip('\r')))  

    pre_val = measurements[0]
    cur_val = measurements[1]

    while True:
        if cur_val > pre_val:
            counter += 1 

        if(ndx >= len(measurements)-1):
            break
        else:
            pre_val = cur_val
            cur_val = measurements[ndx+1]
            ndx += 1
            
    # Print counter
    print(counter)


if __name__ == "__main__":
    # This is executed when run from the command line
    main()
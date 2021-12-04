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
import csv

# Constants
OWNP = os.path.abspath(os.path.dirname(sys.argv[0])) # Own path

def main():
    
    hor = 0
    depth = 0
    aim = 0

    with open(OWNP + '/input.txt', newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=" "))

    for ndx, value in enumerate(data):
        if(value[0] == 'forward'):
            hor += int(value[1])
            depth += aim * int(value[1])
        elif(value[0] == 'down'):
            aim += int(value[1])
        else:
            aim -= int(value[1])

    print(hor * depth)

if __name__ == "__main__":
    # This is executed when run from the command line
    main()
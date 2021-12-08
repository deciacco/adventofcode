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

def rating(data, sensor):
    width = len(max(data[1], key=len))
    winner = ''
    cn_one = 0
    cn_zero = 0
    
    if sensor == 'generator':
        switch_zero = '0'
        switch_one = '1'
    elif sensor == 'scrubber':
        switch_zero = '1'
        switch_one = '0'

    for i in range(width):
        if len(data) > 1:
            for x in range(len(data)):
                if (data[x][0][i] == '1'):
                    cn_one += 1
                else:
                    cn_zero += 1
        
            if cn_one >= cn_zero:
                winner = switch_zero
            else:
                winner = switch_one

            for y in range( len(data) - 1, -1, -1):
                if (data[y][0][i] != winner):
                    del data[y]
        
            cn_zero = 0
            cn_one = 0

    return int(data[0][0], 2)

def main():

    with open(OWNP + '/input.txt', newline='') as csvfile:
        input = list(csv.reader(csvfile, delimiter=" "))

    oxy = rating(input.copy(), 'generator')
    coz = rating(input.copy(), 'scrubber')

    print(oxy * coz)

if __name__ == "__main__":
    # This is executed when run from the command line
    main()
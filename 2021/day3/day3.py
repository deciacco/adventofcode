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

    with open(OWNP + '/input.txt', newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=" "))

    width = len(max(data[1], key=len))

    gamma = ''
    epsilon = ''

    cn_one = 0
    cn_zero = 0

    for i in range(width):
        for x in range(len(data)):
            if (data[x][0][i] == '1'):
                cn_one += 1
            else:
                cn_zero += 1
       
        if cn_one > cn_zero:
            gamma += '1'
            epsilon += '0'
        else:
            epsilon += '1'
            gamma += '0'

        cn_zero = 0
        cn_one = 0

    print("gamma:%s - epsilon:%s" % (gamma, epsilon))
    print("gamma:%i - epsilon:%i" % (int(gamma,2), int(epsilon,2)))
    print("power consumption: %i" % (int(gamma,2) * int(epsilon,2)))

if __name__ == "__main__":
    # This is executed when run from the command line
    main()
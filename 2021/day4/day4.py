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
    
    bingo_nums = []
    bingo_cards = []
    pct = 0
    rct = 0
    cct = 0

    with open(OWNP + '/tempinput.txt', 'r') as f:
        for line in f.readlines()[2:]:
            if line.startswith('\n'):
                pct += 1
                rct = 0
            else:
                for nm in line.split(' '):
                    if nm != '':
                        bingo_cards.append([int(nm.rstrip('\n')), str(pct)+str(rct)+str(5), str(pct)+str(5)+str(cct)])
                        cct += 1
                rct += 1
            cct = 0        
            
    with open(OWNP + '/tempinput.txt', 'r') as f:
        for nm in f.readline().rstrip('\n').split(','):
                bingo_nums.append(int(nm))
    
    for nm in bingo_nums:
        for item in range(0, len(bingo_cards)):
            #if nm == bingo_cards[item][0]:
                print(bingo_cards[item])

    

if __name__ == "__main__":
    # This is executed when run from the command line
    main()
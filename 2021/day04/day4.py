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
FILENM = '/tempinput.txt'
COL  = 5

def main():
    
    bingo_nums = []
    bingo_cards = []
    bingo_record = {}
    pct = 0
    rct = 0
    cct = 0
    winning_board = -1
    non_sel_sum = 0

    with open(OWNP + FILENM, 'r') as f:
        for line in f.readlines()[2:]:
            if line.startswith('\n'):
                pct += 1
                rct = 0
            else:
                for nm in line.split(' '):
                    if nm != '':
                        adrs_row = str(pct)+"."+str(rct)+"."+str(COL)
                        adrs_col = str(pct)+"."+str(COL)+"."+str(cct)

                        bingo_cards.append([int(nm.rstrip('\n')), adrs_row, adrs_col, 0])
                        
                        if adrs_row not in bingo_record and adrs_col not in bingo_record:
                            bingo_record[adrs_row] = 0
                            bingo_record[adrs_col] = 0
                        
                        cct += 1
                rct += 1
            cct = 0        

    with open(OWNP + FILENM, 'r') as f:
        for nm in f.readline().rstrip('\n').split(','):
                bingo_nums.append(int(nm))

    for nm in bingo_nums:
        for item in range(0, len(bingo_cards)):
            if nm == bingo_cards[item][0]:
                bingo_cards[item][3] = 1
                bingo_record[bingo_cards[item][1]] += 1
                bingo_record[bingo_cards[item][2]] += 1

                if bingo_record[bingo_cards[item][1]] == COL or bingo_record[bingo_cards[item][2]] == COL:
                    winning_board = int(bingo_cards[item][1].split(".")[0])
                    break

        if bingo_record[bingo_cards[item][1]] == COL or bingo_record[bingo_cards[item][2]] == COL:
            break

    for item in range(0, len(bingo_cards)):
        if winning_board == int(bingo_cards[item][1].split(".")[0]):
            if bingo_cards[item][3] != 1:
                non_sel_sum += bingo_cards[item][0]

    print(non_sel_sum)
    print(non_sel_sum*nm)

if __name__ == "__main__":
    main()
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'stockPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stocksProfit
#  2. LONG_INTEGER target
#

def stockPairs(stocksProfit, target):
    visited = set()
    valid_pairs = set()
    ret = 0
    for value in stocksProfit:
        diff = target - value
        if diff in visited:
            if (diff, value) not in valid_pairs and (value, diff) not in valid_pairs:
                ret = ret + 1
                valid_pairs.add((diff, value))
        visited.add(value)
    return ret
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stocksProfit_count = int(input().strip())

    stocksProfit = []

    for _ in range(stocksProfit_count):
        stocksProfit_item = int(input().strip())
        stocksProfit.append(stocksProfit_item)

    target = int(input().strip())

    result = stockPairs(stocksProfit, target)

    fptr.write(str(result) + '\n')

    fptr.close()

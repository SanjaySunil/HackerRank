#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    candles = sorted(candles)
    tallest_candle = 0
    count = 0
    for i in range(len(candles)-1, -1, -1):
        if i == len(candles) -1: 
            tallest_candle = candles[i]
            count+=1
        else:
            if candles[i] == tallest_candle: count+=1
            else: break
            
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

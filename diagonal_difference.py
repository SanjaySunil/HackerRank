#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    left = []
    right = []

    for index in range(0, len(arr)):
        left.append(arr[index][index])
    x = 0
    for index in range(len(arr) - 1, -1, -1):
        right.append(arr[x][index])
        x = x + 1

    left_t = 0
    right_t = 0

    for i in left:
        left_t = left_t + i
    for i in right:
        right_t = right_t + i

    return abs(left_t - right_t)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

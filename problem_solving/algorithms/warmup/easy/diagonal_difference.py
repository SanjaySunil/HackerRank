#!/bin/python3
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
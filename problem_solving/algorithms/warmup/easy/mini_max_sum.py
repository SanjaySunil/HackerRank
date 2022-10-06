#!/bin/python3
def miniMaxSum(arr):
    arr = sorted(arr)
    min = 0
    max = 0
    for i in range(1, len(arr)):
        max = max + arr[i]
    for i in range(0, len(arr)-1):
        min = min + arr[i]
    print(min, max)
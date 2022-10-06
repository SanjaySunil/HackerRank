#!/bin/python3
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1

    print(float(positive/len(arr)))
    print(float(negative/len(arr)))
    print(float(zero/len(arr)))
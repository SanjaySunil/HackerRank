#!/bin/python3
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for index in range(0, 3):
        if a[index] > b[index]:
            alice = alice + 1
        elif a[index] < b[index]:
            bob = bob + 1
    return [alice, bob]
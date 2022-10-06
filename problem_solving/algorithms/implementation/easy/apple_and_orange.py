#!/bin/python3
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0
    for apple in apples:
        apple_location = apple + a
        if apple_location >= s and apple_location <= t:
            count_apples += 1

    for orange in oranges:
        orange_location = orange + b
        if orange_location >= s and orange_location <= t:
            count_oranges += 1

    print(count_apples)
    print(count_oranges)
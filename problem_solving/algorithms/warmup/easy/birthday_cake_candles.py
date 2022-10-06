#!/bin/python3
def birthdayCakeCandles(candles):
    candles = sorted(candles)
    tallest_candle = 0
    count = 0
    for i in range(len(candles)-1, -1, -1):
        if i == len(candles) - 1:
            tallest_candle = candles[i]
            count += 1
        else:
            if candles[i] == tallest_candle:
                count += 1
            else:
                break

    return count
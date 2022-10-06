#!/bin/python3
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v2 > v1:
        return 'NO'
    else:
        while x1 != x2:
            if x1 > 10000*10000 or x2 > 10000*10000:
                return 'NO'
            else:
                x1 += v1
                x2 += v2
        return 'YES'
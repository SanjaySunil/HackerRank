#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    new_format = ''
    stamp = s[-2:]
    hour = int(s[0:2])
    if stamp == 'PM':
        if hour != 12:
            new_format = str(12+hour) + s[2:].replace('PM', '')
        else:
            new_format = '12' + s[2:].replace('PM', '')
    else:
        if hour != 12:
            new_format = s[0:].replace('AM', '')
        else:
            new_format = '00' + s[2:].replace('AM', '')
    return new_format


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

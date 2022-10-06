#!/bin/python3
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

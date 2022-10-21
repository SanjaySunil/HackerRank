def pangrams(s):
    flag = 'pangram'
    for i in range(97, 123):
        if chr(i) not in s.lower(): flag = 'not pangram'
    return flag

def gameOfThrones(s):
    s = list(sorted(s))
    unique = list(set(s))
    oneOnly = True
    for i in range(len(unique)):
        if s.count(unique[i]) % 2 != 0 and oneOnly == True: oneOnly = False
        elif s.count(unique[i]) % 2 != 0 and oneOnly == False: return 'NO'
    return 'YES'

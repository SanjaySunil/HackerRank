def superReducedString(s):
    pairsFound = True
    s = list(s)
    while pairsFound == True:
        pairsFound = False
        for i in range(len(s)):
            if i >= len(s)-1: break
            if s[i] == s[i+1]: 
                pairsFound = True
                for _ in range(2): s.pop(i)
    if len(s) == 0: return 'Empty String'
    else: return ''.join(s)

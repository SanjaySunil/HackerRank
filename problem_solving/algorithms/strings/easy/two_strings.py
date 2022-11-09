def twoStrings(s1, s2):
    s1_set = list(set(s1))
    s2_set = list(set(s2))
    
    for i in range(len(s1_set)):
        if s1_set[i] in s2_set: return "YES"
        
    return "NO"

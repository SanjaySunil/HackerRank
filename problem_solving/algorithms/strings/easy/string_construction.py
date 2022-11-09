def stringConstruction(s):
    built_string = ""
    cost = 0
    for i in range(len(s)):
        if s[i] not in built_string:
            cost += 1
            built_string+=s[i]
        else: built_string+=s[i]
    return cost

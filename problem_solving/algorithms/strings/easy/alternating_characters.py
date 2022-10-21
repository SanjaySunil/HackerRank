def alternatingCharacters(s):
    count = 0
    for i in range(len(s)):
        if i == len(s) - 1: break
        if s[i+1] == s[i]: count += 1
    return count

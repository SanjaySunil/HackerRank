def repeatedString(s, n):
    occ = s.count('a')
    remainder = n // len(s)
    return occ * remainder + s[0:n % len(s)].count('a')

def superDigit(n, k):
    if len(n) == 1: return int(n)
    arr = list(n)
    for i in range(len(arr)): arr[i] = int(arr[i])
    total = 0
    for i in range(len(arr)): total += arr[i]
    total = total * k
    k = 1    
    return superDigit(str(total), k)

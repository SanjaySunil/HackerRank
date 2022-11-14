def pickingNumbers(a):
    combinations = []
    a = list(sorted(a))
    for i in range(len(a)):
        for j in range(i, len(a)):
            substring = a[i:j+1]
            if substring != [] and substring[-1] - substring[0] <= 1 and substring[-1] - substring[0] > -1: combinations.append(substring)
    return len(max(combinations, key=len))

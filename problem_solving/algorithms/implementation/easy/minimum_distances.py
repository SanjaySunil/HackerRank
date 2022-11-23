def minimumDistances(a):
    unique_nums = list(set(a))
    pairs = []
    distances = []
    for i in range(len(unique_nums)):
        if a.count(unique_nums[i]) >= 2: pairs.append(unique_nums[i])
    if len(pairs) == 0: return -1
    for i in range(len(pairs)):
        for j in range(len(a)-1, -1, -1):
            if a[j] == pairs[i]: 
                distances.append(abs(j-a.index(pairs[i])))
                break
    return min(distances)

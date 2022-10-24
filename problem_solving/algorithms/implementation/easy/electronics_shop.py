def getMoneySpent(keyboards, drives, b):
    combos = []
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i] + drives[j] <= b: combos.append(keyboards[i] + drives[j])
    if len(combos) == 0: return -1
    else: return max(combos)

def birthday(s, d, m):
    combos = []
    combo_count = 0
    for i in range(len(s)): 
        if len(s[i:i+m]) == m: combos.append(s[i:i+m])
            
    for i in range(len(combos)):
        total = 0
        for j in range(len(combos[i])): total+= combos[i][j]
        if total == d: combo_count+=1
        
    return combo_count

def jumpingOnClouds(c, k):
    cursor = '0'
    energy = 100
            
    while cursor != 0:
        if cursor == '0': cursor = 0
        cursor += k
        energy -= 1
        if cursor >= len(c): cursor = cursor - len(c)
        if c[cursor] == 1: energy -= 2
        
    return energy

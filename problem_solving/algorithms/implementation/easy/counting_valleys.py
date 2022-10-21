def countingValleys(steps, path):
    valleys = 0
    altitude = 0
    for i in range(steps):
        if path[i] == 'D': altitude -= 1
        elif path[i] == 'U' and altitude == -1: valleys, altitude = valleys + 1, altitude + 1
        elif path[i] == 'U': altitude += 1
            
    return valleys

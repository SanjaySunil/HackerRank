def viralAdvertising(n):  
    shares = 5
    likes = shares // 2
    cumulative = 0
    for day in range(0, n):
        if day+1 == 1:
            shares = 5
            likes = shares // 2
        else:
            shares = likes * 3
            likes = shares // 2
        cumulative+=likes
    return cumulative

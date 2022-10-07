def getTotalX(a, b):
    factors = []
    for i in range(1, min(b)+1):
        if all(j % i == 0 for j in b) and all(i % k == 0 for k in a):
            factors.append(i)
        
    return len(factors)

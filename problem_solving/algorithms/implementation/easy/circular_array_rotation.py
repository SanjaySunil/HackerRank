def circularArrayRotation(a, k, queries):
    b = []
    k = k % len(a)
    temp = a[0-k:]
    first = a[:0-k]
    a = temp + first
    [b.append(a[i]) for i in queries]
    return b

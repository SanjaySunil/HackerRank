def permutationEquation(p):
    arr = []
    [arr.append(p.index(p.index(i)+1)+1) for i in range(1, len(p)+1)]
    return arr

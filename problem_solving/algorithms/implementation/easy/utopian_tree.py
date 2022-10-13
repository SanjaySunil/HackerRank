def utopianTree(n):
    height = 0    
    for i in range(0, n+1):
        if i % 2 == 0: height+=1
        else: height*=2
    return height

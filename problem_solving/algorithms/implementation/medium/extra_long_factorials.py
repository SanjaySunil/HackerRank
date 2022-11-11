def extraLongFactorials(n):
    answer = n
    for i in range(n-1, 0, -1): answer = answer * i
    print(answer)

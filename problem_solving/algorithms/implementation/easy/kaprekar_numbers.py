def kaprekarNumbers(p, q):
    ls = []
    for i in range(p, q+1):
        num = str(pow(i, 2))
        if len(num) == 1 and i == 1 or len(num) > 1 and int(num[:len(num) // 2]) + int(num[len(num) // 2:]) == i:
            ls.append(str(i))
    print(" ".join(ls)) if len(ls) > 0 else print('INVALID RANGE')

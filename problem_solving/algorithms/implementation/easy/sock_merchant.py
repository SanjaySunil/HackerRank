def sockMerchant(n, ar):
    ar = sorted(ar)
    pair_list = []
    c = 0
    for i in range(len(ar)):
        if ar[i] not in pair_list: pair_list.append(ar[i])
        elif ar[i] in pair_list:
            c+=1
            pair_list.remove(ar[i])
    return c

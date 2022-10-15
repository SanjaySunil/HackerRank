def angryProfessor(k, a):
    late = 0
    for i in range(len(a)):
        if str(a[i])[0] == '-' or int(str(a[i])[0]) == 0: late+=1
    if late >= k: return 'NO'
    else: return 'YES'

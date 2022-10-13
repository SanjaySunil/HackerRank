def beautifulDays(i, j, k):
    beautiful_days = 0
    for i in range(i, j+1):
        integer = str((i - int(str(i)[::-1])) / k)
        if float(integer) == round(float(integer)): beautiful_days+=1
            
    return beautiful_days

def findDigits(n):
    n_to_string = str(n)
    count = 0
    for d in n_to_string: 
        if int(d) != 0 and n % int(d) == 0: count+=1
    return count

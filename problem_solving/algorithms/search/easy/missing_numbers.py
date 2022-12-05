def missingNumbers(arr, brr):
    brr_set = set(brr)
    return [i for i in brr_set if arr.count(i) != brr.count(i)]  

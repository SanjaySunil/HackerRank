def closestNumbers(arr):
    arr = sorted(list(arr))
    temp = []
    for i in range(len(arr)):
        if i == len(arr) - 1: break
        temp.append(abs(arr[i] - arr[i+1]))
    min_diff = min(temp)
    temp = []
    for i in range(len(arr)):
        if i == len(arr) - 1: break
        if abs(arr[i] - arr[i+1]) == min_diff: 
            temp.append(arr[i])
            temp.append(arr[i+1])
    return temp


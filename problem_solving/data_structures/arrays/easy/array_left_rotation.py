def rotateLeft(d, arr):
    for i in range(d):
        temp = arr[1:]
        temp.append(arr[0])
        arr = temp
    return arr

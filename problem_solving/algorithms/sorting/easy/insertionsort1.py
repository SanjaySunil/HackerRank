def insertionSort1(n, arr):
    insert = arr[-1]
    curr = n - 1
    while True:
        if arr[curr-1] >= insert and curr > 0: arr[curr] = arr[curr-1]
        else: 
            arr[curr] = insert
            print(' '.join(str(i) for i in arr))
            break
        curr -= 1
        print(' '.join(str(i) for i in arr))

def hourglassSum(arr):
    sums = []
    for row in range(4):
        for grid in range(4):
            calc = arr[row][grid] + arr[row][grid+1] + arr[row][grid+2] + arr[row+1][grid+1] + arr[row+2][grid] + arr[row+2][grid+1] + arr[row+2][grid+2] 
            sums.append(calc)
            
    return max(sums)

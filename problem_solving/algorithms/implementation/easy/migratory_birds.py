def migratoryBirds(arr):
    set_arr = set(arr)
    max_list = [0, 0]
    for i in set_arr: 
        if arr.count(i) > max_list[-1]: max_list = [i, arr.count(i)]
    return max_list[0]

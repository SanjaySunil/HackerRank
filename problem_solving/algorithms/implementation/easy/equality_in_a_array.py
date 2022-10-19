def equalizeArray(arr):
    original_length = len(arr)
    key = max(arr, key=arr.count)
    arr = [i for i in arr if i == key]
    return original_length-len(arr)

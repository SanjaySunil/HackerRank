def cutTheSticks(arr):
    answer = []
    while len(arr) != 0:
        answer.append(len(arr))
        shortest = min(arr)
        arr.pop(arr.index(shortest))
        arr = [i-shortest for i in arr]
        arr = [i for i in arr if i > 0]
        
    return answer

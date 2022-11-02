def gemstones(arr):
  count = 0
  for i in range(ord("a"), ord("z")+1):
    flag = True
    for index in range(len(arr)): 
        if chr(i) not in arr[index]: flag = False
    if flag == True: count+=1
  
  return count

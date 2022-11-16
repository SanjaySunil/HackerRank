def compare_lists(llist1, llist2):
    list_1_data = []
    list_2_data = []
    
    while llist1.next != None:
        list_1_data.append(llist1.data)
        llist1 = llist1.next
        
    while llist2.next != None:
        list_2_data.append(llist2.data)
        llist2 = llist2.next
        
    if list_1_data == list_2_data: return 1
    else: return 0

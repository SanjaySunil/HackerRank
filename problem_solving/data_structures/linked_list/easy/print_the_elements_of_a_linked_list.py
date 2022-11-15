def printLinkedList(head):
    while hasattr(head, 'next'):
        print(head.data)
        head = head.next

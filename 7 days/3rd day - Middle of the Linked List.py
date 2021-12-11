def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
##    temp=head
##    cnt=0
##    while(temp):
##        cnt+=1
##        temp=temp.next
##    cnt = cnt // 2
##    while cnt > 0:
##        cnt -= 1
##        head = head.next
##    return head

## Fast and Slow Pointer
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

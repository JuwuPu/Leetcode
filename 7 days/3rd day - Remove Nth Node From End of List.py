class Solution(object):
    def NthFromStart(self,head,n):
        temp=head
        cnt=0
        while(temp):
            cnt+=1
            temp=temp.next
        return cnt-n
    
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        n = self.NthFromStart(head,n)
        current_id = 0
        current_node = head
        previous_node = None
        
        while current_node is not None:
            if current_id == n:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                    return head
                else:
                    head = current_node.next
                    # we don't have to look any further
                    return head
            
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1

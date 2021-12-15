# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## iteration
        # if not head or not head.next:
        #     return head
        # pre,tmp=None,None
        # while(head):
        #     tmp=head.next
        #     head.next=pre
        #     pre=head
        #     head=tmp
        # return pre
        
        ## recursive
        if not head or not head.next:
            return head
        tmp = head.next
        pre = self.reverseList(head.next)
        tmp.next = head
        head.next = None
        return pre

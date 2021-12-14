# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val <= l2.val:
            node = l1
            node.next = self.mergeTwoLists(l1.next,l2)
        else:
            node = l2
            node.next = self.mergeTwoLists(l1,l2.next)
        return node

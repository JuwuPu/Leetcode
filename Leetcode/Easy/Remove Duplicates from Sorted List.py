# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None

class Solution1:
    def list_generate(self, lst):
        """
        生成链表
        """
        if not lst:
            return None
        list_node = ListNode()
        list_node.val = lst[0]
        if len(lst) == 1:
            list_node.next = None
        else:
            list_node.next = self.list_generate(lst[1:])
        return list_node

head = Solution1().list_generate([1,1,2])

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        last, cur = head, head.next
        while True:
            while cur and cur.val == last.val:
                cur = cur.next
            last.next = cur
            last = cur
            if not cur: break
            cur = cur.next
        return head



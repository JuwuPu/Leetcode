# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         val = []
#         temp = 0
#
#         for i in zip(l1,l2):
#             val.append(sum(i))
#         val += max(l1,l2)[len(list(zip(l1,l2))):]
#
#         for j, num in enumerate(val):
#             if num + temp > 10:
#                 val[j] = num % 10 + temp
#                 temp = 1
#             elif num + temp == 10:
#                 val[j] = 0
#                 temp = 1
#             else:
#                 val[j] = num + temp
#                 temp = 0
#         if temp == 1:
#             val += [1]
#         return val
# print(Solution().addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))
# print(Solution().addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = ListNode(0)
        v = val
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            v.next = ListNode(s % 10)
            v = v.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        if (carry > 0):
            v.next = ListNode(1)
        return val.next


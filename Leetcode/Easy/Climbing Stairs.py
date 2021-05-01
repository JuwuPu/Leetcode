class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # val_list = [[0]]
        # for i in range(n):
        #     length = len(val_list[i])
        #     temp_list = []
        #     for j in range(length):
        #         temp_list.append(val_list[i][j]+1)
        #         temp_list.append(val_list[i][j]+2)
        #     val_list.append(temp_list)
        #
        # cnt = 0
        # for item in range(n//2,n+1):
        #     for num in val_list[item]:
        #         if num == n:
        #             cnt += 1
        # return cnt

        if n <= 2: return n
        i1, i2 = 1, 2
        for i in range(2,n):
            temp = i1 + i2
            i1 = i2
            i2 = temp
        return i2


for n in range(1,14):
    print(Solution().climbStairs(n))


# class Node(object):
#     def __init__(self,left=None, right=None, val=None):
#         self.left = left
#         self.right = right
#         self.val = val
#
# class Tree(object):
#     """树类"""
#     def __init__(self):
#         self.root = None
#
#     def add_node(self):
#         node = Node(0)
#         if self.root is None:
#             self.root = node
#         temp_node = self.root
#         while True:
#             root_val = temp_node.val
#             # temp_node.left = Node(val=root_val+1)
#             # temp_node.right = Node(val=root_val+2)
#             node_left = temp_node.left
#             node_right = temp_node.right
#             node_left = Node(val=root_val+1)
#             node_right = Node(val=root_val+2)




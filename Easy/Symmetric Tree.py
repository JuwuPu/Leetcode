# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def check(node1, node2):
        #     if not node1 and not node2:
        #         return False
        #     elif not node1 or not node2:
        #         return False
        #     elif node1.val != node2.val:
        #         return False
        #     else:
        #         return check(node1.left,node2.right) and check(node1.right,node2.left)
        # return check(root,root)

        queue = [root]
        while (queue):
            next_queue = list()
            layer = list()
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)

                layer.append(node.val)

            if layer != layer[::-1]:
                return False
            queue = next_queue

        return True
# Given an integer array nums where the elements are sorted in ascending order,
#   convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of the two
#   subtrees of every node never differs by more than one.


# Constraints:
# · 1 <= nums.length <= 104
# · -104 <= nums[i] <= 104
# · nums is sorted in a strictly increasing order.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
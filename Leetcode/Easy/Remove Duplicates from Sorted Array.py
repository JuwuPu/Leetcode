class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i +1

# class Solution:
#     def removeDuplicates(self, nums):
#         lenth = len(nums)-1
#         if lenth > 0:
#             for i in range(lenth):
#                 if nums[lenth-i] == nums[lenth-i-1]:
#                     del nums[lenth-i-1]
#         return len(nums)







print(Solution().removeDuplicates(([0,0,1,1,1,2,2,3,3,4])))
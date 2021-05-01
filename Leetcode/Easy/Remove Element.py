class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for l in range(len(nums)):
            if nums[i] == val:
                del(nums[i])
            else:
                i += 1
        return len(nums), nums

print(Solution().removeElement([0,0,1,1,1,2,2,3,3,4],0))
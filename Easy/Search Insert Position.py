class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left, right, ans = 0, n-1, n
        while right >= left:
            mid = ((right-left) >> 1) + left
            if target <= nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


print(Solution().searchInsert(nums = [1,3,5,6], target = 8))
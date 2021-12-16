class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        
        for x in nums:
            a, b = b, max(a+x, b)
            print(a,b)
        return b

print(Solution().rob([2,7,9,6,1]))

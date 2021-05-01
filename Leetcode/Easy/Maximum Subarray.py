class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 暴力算法
        # ans = nums[0]
        # length = len(nums)
        # for i in range(length):
        #     for j in range(i,length):
        #         ans = max(ans, sum(nums[i:j+1]))
        # return ans

        # 动态规划
        # pre, ans = 0, nums[0]
        # for i in nums:
        #     pre = max(pre+i, i)     # f(n) 与 f(n-1) 的关系
        #     ans = max(ans, pre)
        # return ans

        # 贪心算法
        # ans = min(nums)
        # pre = 0
        # for i in range(len(nums)):
        #     pre += nums[i]
        #     ans = max(ans, pre)
        #     if pre < 0:
        #         pre = 0
        # return ans

        # 分治法




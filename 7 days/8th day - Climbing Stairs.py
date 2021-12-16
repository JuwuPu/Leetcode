class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 :
            return 0
        elif n == 1 :
            return 1
        elif n == 2 :
            return 2
        else:
            one_step = 2
            two_step = 1
            cnt = 0
            for i in range(2,n):
                cnt = one_step + two_step
                two_step = one_step
                one_step = cnt
            return cnt

print(Solution().climbStairs(10))

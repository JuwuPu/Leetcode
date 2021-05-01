class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        pre = ''
        cur = '1'
        for _ in range(1,n):
            pre = cur
            cur = ''
            i, j = 0, 0
            while j < len(pre):
                while j < len(pre) and pre[i] == pre[j]:
                    j += 1
                cur += str(j-i) + pre[i]
                i = j
        return cur






print(Solution().countAndSay(10))







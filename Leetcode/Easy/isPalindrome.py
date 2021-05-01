# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         return bool(str(x) == str(x)[::-1])



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0 or x % 10 == 0) and x != 0:
            return False
        rev_num = 0
        while x > rev_num:
            rev_num = rev_num * 10 + x % 10
            x = int(x / 10)
        return x == rev_num or x == int(rev_num / 10)

print(Solution().isPalindrome(0))
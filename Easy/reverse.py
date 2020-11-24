class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = ''
        n = len(str(x))
        x_str = list(str(x))
        if 49 <= ord(x_str[0]) <= 57:
            for i in range(n):
                rev += x_str.pop()
            return int(rev) if -2147483648 < x < 2147483647 else 0
        else:
            rev += x_str[0]
            for i in range(n-1):
                rev += x_str.pop()
            return int(rev) if -2147483648 < x < 2147483647 else 0


# class Solution(object):
#     def reverse(self, x):
#         if -10 < x < 10:
#             return x
#         str_x = str(x)
#         if str_x[0] != "-":
#             str_x = str_x[::-1]
#             x = int(str_x)
#         else:
#             str_x = str_x[:0:-1]
#             x = int(str_x)
#             x = -x
#         return x if -2147483648 < x < 2147483647 else 0

print(Solution().reverse(1534236469))
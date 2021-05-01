# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         for i in range(len(haystack)-len(needle) + 1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i
#         return -1

# KMP algorithm

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        next = self.get_next(needle)
        p = 0
        for q in range(len(haystack)):
            while p > 0 and needle[p] != haystack[q]:   # KMP核心 卡点匹配
                p = next[p-1]
            if needle[p] == haystack[q]:                # 首字母比较
                p += 1
            if p == len(needle):                        # 模式串完全匹配判断
                return q - len(needle) + 1
        return -1

    def get_next(self, s):
        j = 0                               # 前缀指针
        next = ['' for i in range(len(s))]
        next[0] = j
        for i in range(1, len(s)):          # 后缀指针
            while j > 0 and s[i] != s[j]:
                j = next[j-1]
            if s[i] == s[j]:
                j += 1
            next[i] = j                      # j ---> 最大前缀数
        return next

print(Solution().get_next("issip"))
print(Solution().strStr(haystack = "mississippi", needle = "issip"))
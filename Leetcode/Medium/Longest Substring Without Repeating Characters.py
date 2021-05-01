# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) == 0:
#             return 0
#         length = 1
#         for i in range(len(s)):
#             ans = 1
#             for j in range(i+1,len(s)):
#                 if not s[j] in s[i:j]:
#                     ans += 1
#                 else:
#                     break
#             if ans >= length:
#                 length = ans
#         return length         5%
#
#         # 哈希集合，记录每个字符是否出现过
#         occ = set()
#         n = len(s)
#         # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
#         rk, ans = -1, 0
#         for i in range(n):
#             if i != 0:
#                 # 左指针向右移动一格，移除一个字符
#                 occ.remove(s[i - 1])
#             while rk + 1 < n and s[rk + 1] not in occ:
#                 # 不断地移动右指针
#                 occ.add(s[rk + 1])
#                 rk += 1
#             # 第 i 到 rk 个字符是一个极长的无重复字符子串
#             ans = max(ans, rk - i + 1)
#         return ans                70%

class Solution():
    def lengthOfLongestSubstring(self, s):
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i - k)
        return res          # 90%

print(Solution().lengthOfLongestSubstring("pwpwek"))
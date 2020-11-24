# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         lcp = ''
#         for i in range(len(min(strs))):
#             for j in range(len(strs)):
#                 if j+1 < len(strs) and strs[j][i] != strs[j+1][i]:
#                     return lcp
#             lcp += strs[0][i]

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         s1 = min(strs)
#         s2 = max(strs)
#         for i,x in enumerate(s1):
#             if x != s2[i]:
#                 return s2[:i]
#         return s1

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = ''
        for i in list(zip(*strs)):
            if len(set(i)) == 1:
                lcp += set(i).pop()
            else:
                break
        return lcp





print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))

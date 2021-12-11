def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
##    k, res, c_dict = -1, 0, {}
##    for i, c in enumerate(s): 
##        if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
##            k = c_dict[c]
##            c_dict[c] = i
##            print(k)
##        else:
##            c_dict[c] = i
##            res = max(res, i-k)
##        print(c_dict)
##    return res
    
##    p1 = 0
##    p2 = 0
##    max_len = 0
##    while p1 < len(s) and p2 <= len(s):
##        if len(set(s[p1:p2])) == len(s[p1:p2]):
##            max_len = max(max_len,p2-p1)
##            p2 += 1 
##        else:
##            p1 += 1
##            max_len = max(max_len,p2-p1)
##        print(s[p1:p2],max_len)
##    return max_len

print(lengthOfLongestSubstring("abcadecefb"))

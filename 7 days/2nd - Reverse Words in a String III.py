def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    p1 = 0
    ans = ''
    s = " " + s + ' '
    for p2 in range(len(s)):
        if s[p2] == " " or p2 == len(s)-1:
            string = s[p1:p2][::-1]
            ans += string
            p1 = p2
    return ans[:-1]

    # return " ".join(i[::-1] for i in s.split())

print(reverseWords("Let's take LeetCode contest"))   

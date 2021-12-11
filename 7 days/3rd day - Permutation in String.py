def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
##        from collections import Counter
##        p1 = 0
##        s1_cnt = Counter(s1)
##        while p1 + len(s1) <= len(s2):
##            if Counter(s2[p1:p1+len(s1)]) == s1_cnt:
##                return True
##            else:
##                p1 += 1
##        return False

    def f(c):
        return ord(c) - 97
    
    ct_s, ct_p = [0] * 26, [0] * 26
    for c in s1:
        ct_p[f(c)] += 1
    l = len(s1)
    for c in s2[: l - 1]:
        ct_s[f(c)] += 1
    for i, c in enumerate(s2[l - 1:]):
        ct_s[f(c)] += 1
        if ct_s == ct_p:
            return True
        ct_s[f(s2[i])] -= 1
    return False
                
print(checkInclusion("adc","dcda"))             
        

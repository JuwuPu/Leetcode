class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanNum = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        num = 0
        # s_ = list(s)
        # while len(s_) > 0:
        #     if len(s_) > 1 and romanNum[s_[-1]] > romanNum[s_[-2]]:
        #         num += romanNum[s_.pop()]
        #         num -= romanNum[s_.pop()]
        #         continue
        #     if len(s_) == 0:
        #         return num
        #     num += romanNum[s_.pop()]
        # return num

        for i, n in enumerate(s):
            if i < len(s) - 1 and romanNum[s[i]] < romanNum[s[i+1]]:
                num -= romanNum[n]
            else:
                num += romanNum[n]
        return num

print(Solution().romanToInt("MCMXCIV"))


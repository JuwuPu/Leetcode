class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        i = -1
        while i:
            if digits[i] == 10 and abs(i) == len(digits):
                digits[i] = 1
                digits.append(0)
                break
            if digits[i] == 10:
                digits[i] = 0
                i -= 1
                digits[i] += 1
            else:
                break
        return digits

print(Solution().plusOne([1,2,3]))
print(1)



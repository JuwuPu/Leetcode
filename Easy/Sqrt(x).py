class Solution(object):
    def mySqrt(self, c):
        """
        :type x: int
        :rtype: int
        """
        maxiter = 100
        x = 1
        for i in range(maxiter):
            x = 0.5 * (x + c/x)
        return x
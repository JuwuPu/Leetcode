class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = m
        nums1[m:] = nums2
        while i < n:
            while nums1[j] < nums1[j-1] and j >= 1:
                nums1[j] = nums1[j-1]
                nums1[j-1] = nums2[i]
                j -= 1
            i += 1
            j = m + i

print(Solution().merge([2,0],1,[1],1))



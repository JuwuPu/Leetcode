def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    #return sorted([x**2 for x in nums])

    p1, p2 = 0, len(nums)-1
    ans = [0]*len(nums)
    while p1 <= p2:
        if abs(nums[p1]) <= abs(nums[p2]):
            ans[p2-p1] = nums[p2]**2
            p2 -= 1
        else:
            ans[p2-p1] = nums[p1]**2
            p1 += 1
    return ans
            
    

print(sortedSquares([-5,-3,-2,4]))

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
#    nums[0:len(nums)-k] = nums[0:len(nums)-k][::-1]
#    nums[len(nums)-k:]  =  nums[len(nums)-k:][::-1]
#    nums.reverse()

#    for i in range(k):
#        p1, p2, temp = len(nums)-2, len(nums)-1, 0
#        while p1 != -1:
#            temp = nums[p1]
#            nums[p1] = nums[p2]
#            nums[p2] = temp
#            p1 -= 1
#            p2 -= 1

    n = len(nums)
    k = k % n
    nums[:] = nums[n - k:] + nums[:n - k]
    return nums


print(rotate([1,2,3],3))

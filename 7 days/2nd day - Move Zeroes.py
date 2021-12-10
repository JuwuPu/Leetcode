def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    p1 = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[p1], nums[i] = nums[i], nums[p1]
            p1 += 1


moveZeroes([0,0,1])

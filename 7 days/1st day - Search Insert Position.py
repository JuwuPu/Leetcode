def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] == target:
            return mid
        else:
            left = mid + 1
    return left

print (searchInsert([1,3,5,6],3))

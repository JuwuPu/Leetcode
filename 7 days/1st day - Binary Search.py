def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (high -  low) // 2 + low
        num = nums[mid]
        if num == target:
            return mid
        elif num >= target:
            high = mid -1
        else:
            low = mid + 1
    return -1


print(search([-1,0,3,5,9,12],1))

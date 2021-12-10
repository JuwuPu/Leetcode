def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    p1, p2 = 0, len(numbers)-1
    while p1 + p2 <= len(numbers):
        if numbers[p1] + numbers[p2] < target:
            p1 += 1
        elif numbers[p1] + numbers[p2] == target:
            return [p1+1, p2+1]
        else:
            p2 += 1
    return [p1+1, p2+1]
print(twoSum([-1,0],-1))

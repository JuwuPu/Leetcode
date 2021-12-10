def firstBadVersion(bad, n):
    """
    :type n: int
    :rtype: int
    """
    low = 1
    while low < n:
        mid = low + (n - low) //2 # this formula fast than (low + n) //2 + 1
        if mid == bad:
            n = mid
        else:
            low = mid + 1
    return low

print(firstBadVersion(4,5))
    
        

from bisect import bisect_left, bisect_right

def countFairPairs(nums, lower, upper):
    # Step 1: Sort the array
    nums.sort()
    n = len(nums)
    count = 0
    
    # Step 2: For each element in nums, find the range of pairs that satisfy the conditions
    for i in range(n):
        # Find the range of j values for which lower <= nums[i] + nums[j] <= upper
        left = bisect_left(nums, lower - nums[i], i + 1, n)  # Lower bound index for j
        right = bisect_right(nums, upper - nums[i], i + 1, n) - 1  # Upper bound index for j
        
        # Add the number of valid pairs (i, j) with i < j
        if left <= right:
            count += (right - left + 1)
    
    return count

class Solution(object):
    def minimumMountainRemovals(self, nums):
        n = len(nums)
        
        # Calculate Longest Increasing Subsequence (LIS) ending at each index
        lis = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        # Calculate Longest Decreasing Subsequence (LDS) starting from each index
        lds = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)

        # Find the minimum removals needed to make a mountain array
        min_removals = float('inf')
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:  # Only consider valid peaks
                min_removals = min(min_removals, n - (lis[i] + lds[i] - 1))
        
        return min_removals

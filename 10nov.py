from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_length = float('inf')
        left = 0
        n = len(nums)
        
        for right in range(n):
            current_or = 0
            for j in range(right, left - 1, -1):  # Calculate OR from the right to left
                current_or |= nums[j]
                if current_or >= k:
                    min_length = min(min_length, right - j + 1)
                    break

        return -1 if min_length == float('inf') else min_length

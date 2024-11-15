from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # Step 1: Find the longest sorted prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        
        # If the whole array is sorted
        if left == n - 1:
            return 0
        
        # Step 2: Find the longest sorted suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Minimum removal considering only prefix or suffix
        min_removal = min(n - left - 1, right)
        
        # Step 3: Merge prefix and suffix
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                min_removal = min(min_removal, j - i - 1)
                i += 1
            else:
                j += 1
        
        return min_removal

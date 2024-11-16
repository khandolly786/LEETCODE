from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        results = []
        
        for i in range(len(nums) - k + 1):
            # Get the subarray of size k
            subarray = nums[i:i + k]
            
            # Check if the subarray is sorted and consecutive
            if subarray == list(range(min(subarray), max(subarray) + 1)):
                results.append(max(subarray))
            else:
                results.append(-1)
        
        return results

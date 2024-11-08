from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_value = (1 << maximumBit) - 1  # All bits set to 1 for the given maximumBit
        xor_sum = 0
        
        # Calculate the XOR of all elements initially
        for num in nums:
            xor_sum ^= num
        
        answer = []
        
        # For each query, calculate the optimal k and update xor_sum
        for i in range(len(nums) - 1, -1, -1):
            k = xor_sum ^ max_value
            answer.append(k)
            xor_sum ^= nums[i]  # Remove the last element of nums from xor_sum
        
        return answer

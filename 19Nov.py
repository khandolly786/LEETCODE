from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Initialize variables
        max_sum = 0
        current_sum = 0
        freq_map = {}
        start = 0

        # Iterate through the array using the sliding window
        for end in range(len(nums)):
            # Add the current number to the frequency map and update the sum
            current_num = nums[end]
            freq_map[current_num] = freq_map.get(current_num, 0) + 1
            current_sum += current_num

            # If the window size exceeds k, shrink it
            if end - start + 1 > k:
                left_num = nums[start]
                current_sum -= left_num
                freq_map[left_num] -= 1
                if freq_map[left_num] == 0:
                    del freq_map[left_num]
                start += 1

            # Check if the current window is valid and update max_sum
            if end - start + 1 == k and len(freq_map) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum

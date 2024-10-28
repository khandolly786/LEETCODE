class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use a set for fast square lookups
        num_set = set(nums)
        longest_streak = 0
        
        # Sort nums for sequential streak building
        nums.sort()
        
        for num in nums:
            streak_length = 1
            current = num
            
            # Build the square streak
            while current * current in num_set:
                current *= current
                streak_length += 1
            
            # Update longest streak if it's valid and the longest found
            if streak_length >= 2:
                longest_streak = max(longest_streak, streak_length)
        
        # If no valid streak found, return -1
        return longest_streak if longest_streak >= 2 else -1

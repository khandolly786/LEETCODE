from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Count the total occurrences of each character
        total_count = Counter(s)
        
        # If any character count is less than k, return -1
        if any(total_count[char] < k for char in 'abc'):
            return -1
        
        # Sliding window to find the maximum middle segment that satisfies the condition
        n = len(s)
        max_window_size = 0
        left = 0
        current_count = Counter()
        
        for right in range(n):
            current_count[s[right]] += 1
            
            # Shrink window if there are too many of a character in the window
            while any(current_count[char] > total_count[char] - k for char in 'abc'):
                current_count[s[left]] -= 1
                left += 1
            
            # Update the maximum window size
            max_window_size = max(max_window_size, right - left + 1)
        
        # Minimum minutes needed = total length - maximum middle window size
        return n - max_window_size

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        score = 0
        
        while any(not m for m in marked):
            min_val = None
            min_index = -1
            
            for i in range(n):
                if not marked[i] and (min_val is None or nums[i] < min_val):
                    min_val = nums[i]
                    min_index = i
            
            score += min_val
            marked[min_index] = True
            if min_index - 1 >= 0:
                marked[min_index - 1] = True
            if min_index + 1 < n:
                marked[min_index + 1] = True
        
        return score

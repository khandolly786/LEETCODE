class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_value = float('inf')
        negative_count = 0
        
        for row in matrix:
            for value in row:
                total_sum += abs(value)
                if value < 0:
                    negative_count += 1
                min_value = min(min_value, abs(value))
        
        # If negative count is odd, one negative remains
        if negative_count % 2 == 1:
            total_sum -= 2 * min_value
        
        return total_sum

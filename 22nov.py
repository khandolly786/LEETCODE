from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        pattern_count = defaultdict(int)
        
        for row in matrix:
            # Normalize the row by its first value
            # If the first value is 1, we complement the entire row
            normalized_pattern = tuple(row[i] ^ row[0] for i in range(len(row)))
            pattern_count[normalized_pattern] += 1
        
        # The maximum count in the hashmap is the answer
        return max(pattern_count.values())

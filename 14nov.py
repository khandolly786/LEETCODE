import math
from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Helper function to determine if a maximum load per store `x` is feasible
        def canDistribute(maxLoad):
            stores_needed = 0
            for qty in quantities:
                stores_needed += math.ceil(qty / maxLoad)
            return stores_needed <= n

        # Set the binary search bounds
        left, right = 1, max(quantities)
        
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid  # try for a smaller maximum load
            else:
                left = mid + 1  # increase the load limit
        
        return left

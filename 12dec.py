import heapq
import math

class Solution:
    def pickGifts(self, gifts, k):
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest_pile = -heapq.heappop(max_heap)
            remaining_gifts = math.floor(math.sqrt(largest_pile))
            heapq.heappush(max_heap, -remaining_gifts)

        total_gifts_remaining = -sum(max_heap)
        return total_gifts_remaining

gifts = [25, 64, 9, 4, 100]
k = 4
solution = Solution()
print(solution.pickGifts(gifts, k))

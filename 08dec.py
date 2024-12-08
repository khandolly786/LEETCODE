class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        max_value = 0
        result = 0
        sorted_start = sorted((start, value) for start, _, value in events)
        starts, values = zip(*sorted_start)
        
        for start, end, value in events:
            idx = bisect.bisect_left(starts, end + 1)
            if idx < len(starts):
                result = max(result, value + max_value)
            max_value = max(max_value, value)
            result = max(result, max_value)
        
        return result

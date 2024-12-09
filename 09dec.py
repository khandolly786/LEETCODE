class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        parity_diff = [1 if nums[i] % 2 != nums[i + 1] % 2 else 0 for i in range(n - 1)]
        results = []
        for start, end in queries:
            if end - start == 0:
                results.append(True)
            else:
                results.append(all(parity_diff[start:end]))
        return results

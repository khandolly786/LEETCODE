class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        result = [0] * n
        for i in range(n):
            if k > 0:
                result[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            elif k < 0:
                result[i] = sum(code[(i + j) % n] for j in range(k, 0))
        
        return result

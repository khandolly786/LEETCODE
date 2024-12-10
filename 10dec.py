class Solution:
    def maximumLength(self, s: str) -> int:
        from collections import Counter

        def is_special(sub: str) -> bool:
            return all(ch == sub[0] for ch in sub)

        n = len(s)
        for length in range(n, 0, -1):
            substring_count = Counter()
            for i in range(n - length + 1):
                sub = s[i:i + length]
                if is_special(sub):
                    substring_count[sub] += 1
            for sub, count in substring_count.items():
                if count >= 3:
                    return length
        return -1

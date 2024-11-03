class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if goal is a substring of s + s and if they are the same length
        return len(s) == len(goal) and goal in (s + s)

class Solution(object):
    def maxMoves(self, grid):
        rows, cols = len(grid), len(grid[0])
        dp = [[-1] * cols for _ in range(rows)]

        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            
            max_moves = 0
            for dr, dc in [(0, 1), (1, 1), (-1, 1)]:  # move right, diagonally up-right, diagonally down-right
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > grid[r][c]:
                    max_moves = max(max_moves, 1 + dfs(nr, nc))
            
            dp[r][c] = max_moves
            return max_moves

        result = 0
        for r in range(rows):
            result = max(result, dfs(r, 0))
        
        return result

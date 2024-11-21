from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Create a grid to mark walls and guards
        grid = [[0] * n for _ in range(m)]  # 0 means empty, 1 means wall, 2 means guard

        # Mark the walls
        for wall in walls:
            grid[wall[0]][wall[1]] = 1  # Mark walls as 1
        
        # Mark the guards
        for guard in guards:
            grid[guard[0]][guard[1]] = 2  # Mark guards as 2

        # Directions for north, east, south, west (dy, dx)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Mark the guarded cells
        def mark_guarded(row, col):
            # For each direction, we mark the cells as guarded
            for dy, dx in directions:
                x, y = col, row
                while 0 <= x + dx < n and 0 <= y + dy < m and grid[y + dy][x + dx] != 1 and grid[y + dy][x + dx] != 2:
                    y += dy
                    x += dx
                    grid[y][x] = 3  # Mark as guarded

        # Process each guard
        for guard in guards:
            mark_guarded(guard[0], guard[1])

        # Count unguarded cells
        unguarded_count = 0
        for i in range(m):
            for j in range(n):
                # A cell is unguarded if it's not a wall or guard and not guarded
                if grid[i][j] == 0:
                    unguarded_count += 1

        return unguarded_count

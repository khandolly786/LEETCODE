from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize distance array with infinity
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # Use deque for 0-1 BFS
        dq = deque([(0, 0, 0)])  # (x, y, cost)
        
        while dq:
            x, y, cost = dq.popleft()
            
            # Early exit if reaching the bottom-right corner
            if x == m - 1 and y == n - 1:
                return cost
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]
                    
                    # Only update if we found a cheaper path
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        if grid[nx][ny] == 0:
                            dq.appendleft((nx, ny, new_cost))  # No obstacle, prioritize
                        else:
                            dq.append((nx, ny, new_cost))  # Obstacle, process later
        
        return dist[m - 1][n - 1]

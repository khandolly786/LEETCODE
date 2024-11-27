from collections import deque, defaultdict
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize the graph with the initial roads
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)

        def bfs():
            """Perform BFS to find the shortest path from 0 to n-1."""
            queue = deque([0])
            distances = [-1] * n
            distances[0] = 0
            
            while queue:
                current = queue.popleft()
                
                for neighbor in graph[current]:
                    if distances[neighbor] == -1:  # Not visited
                        distances[neighbor] = distances[current] + 1
                        queue.append(neighbor)
                        # Stop early if we reach the target
                        if neighbor == n - 1:
                            return distances[neighbor]
            return distances[n - 1]  # Return distance to target

        # Process each query and compute the shortest path
        result = []
        for u, v in queries:
            graph[u].append(v)
            result.append(bfs())

        return result

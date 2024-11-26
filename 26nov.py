from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Initialize the in-degree array
        in_degree = [0] * n
        
        # Step 2: Populate in-degree array
        for u, v in edges:
            in_degree[v] += 1
        
        # Step 3: Find nodes with in-degree 0
        champions = [i for i in range(n) if in_degree[i] == 0]
        
        # Step 4: Determine the result
        if len(champions) == 1:
            return champions[0]  # Return the unique champion
        else:
            return -1  # Either no champion or multiple champions

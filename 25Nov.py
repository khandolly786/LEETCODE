from collections import deque

class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        # Convert the 2D board to a 1D string for easier manipulation
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"  # Target configuration

        # Directions for moving the empty tile (0)
        neighbors = {
            0: [1, 3],  # Possible swaps for position 0
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        # BFS initialization
        queue = deque([(start, start.index('0'), 0)])  # (state, zero_index, moves)
        visited = set()
        visited.add(start)

        while queue:
            state, zero_index, moves = queue.popleft()
            
            # If the target configuration is reached
            if state == target:
                return moves
            
            # Explore all possible moves
            for neighbor in neighbors[zero_index]:
                new_state = list(state)
                # Swap the empty tile with the neighbor
                new_state[zero_index], new_state[neighbor] = new_state[neighbor], new_state[zero_index]
                new_state_str = ''.join(new_state)
                
                # If the new state hasn't been visited, add it to the queue
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, neighbor, moves + 1))

        # If no solution is found
        return -1

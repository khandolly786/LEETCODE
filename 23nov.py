class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        # Simulate gravity for each row in the box
        for row in box:
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '#':
                    row[j], row[empty] = row[empty], row[j]
                    empty -= 1
                elif row[j] == '*':
                    empty = j - 1
        
        # Rotate the box 90 degrees clockwise
        rotated = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - i - 1] = box[i][j]
        
        return rotated

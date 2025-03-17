from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Finds the maximum area of an island in the given grid.

        An island is a group of connected 1s (representing land) in a 2D grid.
        The area of an island is the number of connected 1s.

        Args:
            grid: A 2D list representing the grid.

        Returns:
            The maximum area of an island in the grid.
        """        
        if not grid or not grid[0]:
            return 0

        max_area = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 0

            visited.add((r, c))
            area = 1  # current cell
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))

        return max_area
    
grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

# Output: 6

print(Solution().maxAreaOfIsland(grid))

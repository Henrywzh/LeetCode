from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        height, width = len(grid), len(grid[0])
        q = deque()

        # Step 1: enqueue all treasure cells (value 0)
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    q.append((x, y, 0))  # (col, row, steps)

        # Step 2: perform BFS from all treasures simultaneously
        while q:
            x, y, steps = q.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] > steps + 1:
                    grid[ny][nx] = steps + 1
                    q.append((nx, ny, steps + 1))

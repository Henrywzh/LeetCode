from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        q = deque()
        height, width = len(grid), len(grid[0])

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    q.append((j, i, 0))

        while q:
            x, y, t = q.popleft()
            res = max(res, t)  # move this outside the loop

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == 1:
                    grid[ny][nx] = 2
                    q.append((nx, ny, t + 1))

        for row in grid:
            if 1 in row:
                return -1

        return res

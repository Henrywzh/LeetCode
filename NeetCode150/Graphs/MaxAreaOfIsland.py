from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        curr = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y):
            nonlocal curr
            if x < 0 or y < 0 or x >= COLS or y >= ROWS:
                return

            if grid[y][x] == 0:
                return

            grid[y][x] = 0
            curr += 1

            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(j, i)
                    res = max(res, curr)
                    curr = 0
        return res


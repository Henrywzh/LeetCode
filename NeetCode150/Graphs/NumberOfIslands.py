from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        height, width = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= width or y < 0 or y >= height:
                return
            if grid[y][x] == '0':
                return

            grid[y][x] = '0'  # mark as visited

            # explore 4 directions
            dfs(x + 1, y)  # right
            dfs(x - 1, y)  # left
            dfs(x, y + 1)  # down
            dfs(x, y - 1)  # up

        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    res += 1
                    dfs(j, i)

        return res

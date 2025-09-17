from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        1. Find the starting letter first
        2. do traversal
        """
        m, n = len(board), len(board[0])
        length = len(word)

        def dfs(x, y, k):
            if k == length:
                return True
            if not ((0 <= x < n) and (0 <= y < m)) or board[y][x] != word[k]:
                return False

            temp = board[y][x]
            board[y][x] = '*'
            search = (
                    dfs(x + 1, y, k + 1) or
                    dfs(x - 1, y, k + 1) or
                    dfs(x, y + 1, k + 1) or
                    dfs(x, y - 1, k + 1)
            )
            board[y][x] = temp

            return search

        for y in range(m):
            for x in range(n):
                if dfs(x, y, 0):
                    return True

        return False


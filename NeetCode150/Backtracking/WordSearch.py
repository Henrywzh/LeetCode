from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        check = False
        height, width = len(board), len(board[0])

        def dfs(x, y, chars, prev):
            nonlocal check

            if board[x][y] != chars[0]:
                return

            if len(chars) == 1:
                check = True
                return

            if x + 1 < height and (x + 1, y) not in prev:
                dfs(x + 1, y, chars[1:], prev + [(x, y)])
            if x - 1 >= 0 and (x - 1, y) not in prev:
                dfs(x - 1, y, chars[1:], prev + [(x, y)])
            if y + 1 < width and (x, y + 1) not in prev:
                dfs(x, y + 1, chars[1:], prev + [(x, y)])
            if y - 1 >= 0 and (x, y - 1) not in prev:
                dfs(x, y - 1, chars[1:], prev + [(x, y)])

        for i in range(height):
            for j in range(width):
                dfs(i, j, word, [])
                if check:
                    return True

        return False

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        for y in range(9):  # rows
            for x in range(9):  # cols
                if board[y][x] == ".":
                    continue

                if (board[y][x] in rows[y] or board[y][x] in cols[x] or board[y][x] in boxes[3 * (y // 3) + x // 3]):
                    return False

                cols[x].add(board[y][x])
                rows[y].add(board[y][x])
                boxes[3 * (y // 3) + x // 3].add(board[y][x])

        return True
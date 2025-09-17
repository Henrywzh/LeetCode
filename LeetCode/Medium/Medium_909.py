from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # 1) Linearize board into 'arr' with zig-zag numbering (0-based indices)
        arr = []
        left_to_right = True
        for r in range(n - 1, -1, -1):
            row = board[r][:]
            if not left_to_right:
                row.reverse()
            arr.extend(row)
            left_to_right = not left_to_right  # flip direction for next row

        # 2) BFS over positions 0..n*n-1
        target = n * n - 1
        q = deque([(0, 0)])          # (position index, rolls)
        visited = {0}

        while q:
            pos, rolls = q.popleft()
            if pos == target:
                return rolls
            for step in range(1, 7):
                nxt = pos + step
                if nxt > target:
                    continue  # can't move beyond the last square
                # If there is a snake/ladder (value != -1), teleport to dest-1
                if arr[nxt] != -1:
                    nxt = arr[nxt] - 1
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, rolls + 1))

        return -1  # unreachable

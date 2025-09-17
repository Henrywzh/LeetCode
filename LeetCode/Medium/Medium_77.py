from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(cur, i, length):
            if length == k:
                res.append(cur)
                return

            for num in range(i + 1, n + 1):
                dfs(cur + [num], num, length + 1)

        dfs([], 0, 0)
        return res



from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, ns):
            if not ns:
                res.append(curr)
                return

            for i, n in enumerate(ns):
                dfs(curr + [n], ns[:i] + ns[i + 1:])

        dfs([], nums)

        return res

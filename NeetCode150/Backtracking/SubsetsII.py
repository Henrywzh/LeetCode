from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(curr, ns):
            if curr not in res:
                res.append(curr)

            for i, n in enumerate(ns):
                dfs(curr + [n], ns[i + 1:])

        dfs([], nums)

        return res

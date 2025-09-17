from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, candidates):
            if not candidates:
                res.append(cur)
                return

            for c in candidates:
                temp = candidates.copy()
                temp.remove(c)
                dfs(cur + [c], temp)

        dfs([], set(nums))

        return res
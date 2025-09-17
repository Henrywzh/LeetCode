from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def backtrack(xs, i, remaining):
            if remaining == 0:
                res.append(xs)
                return
            elif remaining < 0:
                return
            for idx in range(i, n):
                backtrack(xs + [candidates[idx]], idx, remaining - candidates[idx])

        backtrack([], 0, target)

        return res

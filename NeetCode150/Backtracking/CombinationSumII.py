from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return

            for j in range(i, n):
                val = candidates[j]
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if total + val > target:
                    break

                curr.append(val)
                dfs(j + 1, curr, total + val)
                curr.pop()

        dfs(0, [], 0)

        return res



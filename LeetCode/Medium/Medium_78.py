from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, cur):
            res.append(cur)
            for j in range(i + 1, len(nums)):
                backtrack(j, cur + [nums[j]])

        backtrack(-1, [])
        return res

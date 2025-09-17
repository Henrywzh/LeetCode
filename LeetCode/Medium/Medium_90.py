from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def backtrack(i, cur):
            res.append(cur)

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                backtrack(j, cur + [nums[j]])

        backtrack(-1, [])

        return res


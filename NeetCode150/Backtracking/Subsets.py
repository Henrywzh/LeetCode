from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtracking([], nums)
        return self.res

    def backtracking(self, curr: List[int], nums: List[int]) -> None:
        self.res.append(curr)

        if len(nums) == 0:
            return

        for i, n in enumerate(nums):
            self.backtracking(curr + [n], nums[i + 1:])

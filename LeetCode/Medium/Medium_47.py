from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def backtrack(cur, unseen):
            if len(unseen) == 0:
                res.append(cur)
            for i in range(len(unseen)):
                if i > 0 and unseen[i] == unseen[i - 1]:
                    continue
                new_unseen = unseen[:i] + unseen[i + 1:]
                backtrack(cur + [unseen[i]], new_unseen)

        backtrack([], nums)

        return res


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        guessed = dict()

        for i, n in enumerate(nums):
            guess = target - n
            if n not in guessed:
                guessed[guess] = i
            else:
                return [guessed[n], i]

        return []

"""
Idea
- Since there is only one unique answer, let guess = target - current number,
- guess must appear in nums, it could be before the current number or after
- if it is before, then the dictionary has a record
- if it is after, then record the guess and move on to the next number
"""

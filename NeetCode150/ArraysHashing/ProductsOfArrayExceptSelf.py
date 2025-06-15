from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul = [1]
        right_mul = [1] * len(nums)

        for i, n in enumerate(nums[:-1]):
            left_mul.append(left_mul[i] * n)

        for i in range(len(nums) - 1):
            right_mul[-(i + 2)] = right_mul[-(i + 1)] * nums[-(i + 1)]

        res = []
        for i in range(len(nums)):
            res.append(left_mul[i] * right_mul[i])

        return res


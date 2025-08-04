from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxProd = 1
        minProd = 1

        for i in range(len(nums)):
            tmp = maxProd * nums[i]
            maxProd = max(maxProd * nums[i], minProd * nums[i], nums[i])
            minProd = min(tmp, minProd * nums[i], nums[i])
            res = max(maxProd, res)

        return res

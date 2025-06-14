from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def merge(self, xs: List[int], ys: List[int]) -> List[int]:
        res = []
        i, j = 0, 0

        while i < len(xs) and j < len(ys):
            if xs[i] < ys[j]:
                res.append(xs[i])
                i += 1
            else:
                res.append(ys[j])
                j += 1

        while i < len(xs):
            res.append(xs[i])
            i += 1

        while j < len(ys):
            res.append(ys[j])
            j += 1

        return res

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        xs, ys = nums[:mid], nums[mid:]

        return self.merge(self.mergeSort(xs), self.mergeSort(ys))





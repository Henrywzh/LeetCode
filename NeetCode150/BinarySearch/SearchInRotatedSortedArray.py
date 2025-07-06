from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 0

        while l <= r:
            if nums[l] < nums[r]:
                if nums[res] > nums[l]:
                    res = l

                break

            m = (l + r) // 2
            if nums[res] > nums[m]:
                res = m

            if nums[m] >= nums[l]:  # in the right
                l = m + 1
            else:
                r = m - 1

        return res  # index of the min element

    def search(self, nums: List[int], target: int) -> int:
        idx = self.findMin(nums)
        print(idx)
        if idx == 0:
            l, r = 0, len(nums) - 1
        elif nums[0] <= target <= nums[idx - 1]:
            l, r = 0, idx - 1
        else:
            l, r = idx, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1


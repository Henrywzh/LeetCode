from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        m = (l + r) // 2

        def bs(_nums):
            l, r = 0, len(_nums) - 1
            m = (l + r) // 2

            while l <= r:
                if target < _nums[m]:
                    r = m - 1
                elif target > _nums[m]:
                    l = m + 1
                else:
                    return True

                m = (l + r) // 2

            return False

        while l <= r:
            nums = matrix[m]
            if target < nums[0]:
                r = m - 1
            elif target > nums[-1]:
                l = m + 1
            else:
                return bs(nums)

            m = (l + r) // 2

        return False

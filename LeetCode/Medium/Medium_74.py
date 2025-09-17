from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m - 1

        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                l, r = 0, n - 1
                while l <= r:
                    idx = (l + r) // 2
                    if target < matrix[mid][idx]:
                        r = idx - 1
                    elif target > matrix[mid][idx]:
                        l = idx + 1
                    else:
                        return True
                return False

        return False

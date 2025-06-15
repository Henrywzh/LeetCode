from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i, j = 0, len(heights) - 1

        while i < j:
            area = max((j - i) * min(heights[i], heights[j]), area)
            if heights[i] < heights[j]:  # area only depend on the min height
                i += 1
            else:
                j -= 1

        return area
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # depends on the min height
        prefix, suffix = {0: 0}, {len(height) - 1: 0}
        res = 0

        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i + 1])

        for i in range(len(height)):
            res += max(min(prefix[i], suffix[i]) - height[i], 0)

        return res

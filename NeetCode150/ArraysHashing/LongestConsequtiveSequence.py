from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for n in nums:
            if n - 1 not in numSet:
                # then n is the start of a seq
                i = 1
                while (n + i) in numSet:
                    i += 1
                maxLen = max(i, maxLen)

        return maxLen



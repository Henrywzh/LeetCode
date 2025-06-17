from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            for j in range(i + 1, min(len(nums), i + 1 + k)):
                if nums[i] == nums[j]:
                    return True

        return False
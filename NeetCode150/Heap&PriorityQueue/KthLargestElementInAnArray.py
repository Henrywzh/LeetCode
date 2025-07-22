import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        while k > 1:
            k -= 1
            heapq.heappop(nums)

        return -nums[0]

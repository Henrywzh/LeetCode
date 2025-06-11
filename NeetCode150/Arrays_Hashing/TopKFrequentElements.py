from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for n, cnt in count.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq)):
            if len(res) == k:
                break

            res += freq[len(freq) - i - 1]

        return res

"""
Explanation:
- To achieve O(N) complexity, use bucket sort
- First record all the freq for each distinct n in nums
- Create a freq from 0 to len(nums), group the nums with same freq
- Add the top freq nums first to res, until the len(res) == k
"""

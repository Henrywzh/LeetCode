from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix = {0: prices[0]}  # min
        suffix = {len(prices) - 1: prices[-1]}  # max

        for i in range(1, len(prices)):
            prefix[i] = min(prefix[i - 1], prices[i])
            j = len(prices) - i - 1
            suffix[j] = max(suffix[j + 1], prices[j])

        res = 0

        for i in range(len(prices)):
            res = max(res, suffix[i] - prefix[i])

        return res
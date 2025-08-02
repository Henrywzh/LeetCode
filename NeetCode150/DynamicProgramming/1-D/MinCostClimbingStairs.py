from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [101] * n
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]

        for i in range(3, n + 1):
            dp[-i] = cost[-i] + min(dp[-(i - 1)], dp[-(i - 2)])

        return min(dp[0], dp[1])

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(k):
            if k == 0:
                return 0

            if k in memo:
                return memo[k]

            res = 1e9
            for c in coins:
                if k >= c:
                    res = min(res, 1 + dfs(k - c))

            memo[k] = res

            return res

        res = dfs(amount)

        return -1 if res >= 1e9 else res

"""
You are given an integer array coins representing coins of different denominations 
(e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. 
If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.
"""

def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for target in range(1, amount + 1):
        for c in coins:
            if target >= c:
                dp[target] = min(dp[target], dp[target - c] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1
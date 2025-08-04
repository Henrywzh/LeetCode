from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def dfs(xs):
            if xs == '':
                return True
            if xs in memo:
                return memo[xs]

            for i in range(len(xs)):
                if xs[:i + 1] in wordSet and dfs(xs[i + 1:]):
                    memo[xs] = True
                    return True

            memo[xs] = False
            return False

        return dfs(s)


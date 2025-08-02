class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * n
        res[0] = 1

        for i in range(1, n):
            if i == 1:
                res[i] = 1 + res[i - 1]
            else:
                res[i] = res[i - 1] + res[i - 2]

        return res[-1]

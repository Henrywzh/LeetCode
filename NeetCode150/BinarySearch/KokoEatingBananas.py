from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = int((l + r) / 2)
        res = None

        def eatAll(_k):
            cnt = 0
            for x in piles:
                cnt += -(-x // k)

                if cnt > h:
                    return False

            return True

        while l <= r:
            if eatAll(k):  # r = k - 1
                res = k
                r = k - 1
            else:
                l = k + 1

            k = int((l + r) / 2)

        return res


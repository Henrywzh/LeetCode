import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            fst, snd = heapq.heappop(stones), heapq.heappop(stones)
            if fst != snd:
                heapq.heappush(stones, -abs(fst - snd))
            else:
                continue

        stones.append(0)

        return abs(stones[0])

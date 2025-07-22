import heapq
from collections import deque
from typing import List, Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter[tasks]
        freq = [-cnt for cnt in count.values()]


        heapq.heapify(freq)
        q = deque()

        while freq or q:
            time += 1

            if not freq:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(freq)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(freq, q.popleft()[0])

        return time

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)

        def time(pos, v):
            return (target - pos) / v

        for pos, v in cars:
            if stack and time(pos, v) <= time(stack[-1][0], stack[-1][1]):
                continue

            stack.append((pos, v))

        return len(stack)


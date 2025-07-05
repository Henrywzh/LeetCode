class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        lefts = [-1] * n
        rights = [n] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                lefts[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                rights[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            lefts[i] += 1
            rights[i] -= 1
            area = ((rights[i] - lefts[i]) + 1) * heights[i]
            res = max(res, area)

        return res
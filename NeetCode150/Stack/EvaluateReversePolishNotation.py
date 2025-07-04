from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def cal(l, r, op):
            l, r = int(l), int(r)
            if op == '+':
                return l + r
            elif op == '-':
                return l - r
            elif op == '*':
                return l * r
            else:
                return int(l / r)

        stack = []

        for c in tokens:
            print(stack, c)
            if c not in ['+', '-', '*', '/']:
                stack.append(int(c))
            else:
                l, r = stack[-2], stack[-1]
                stack.pop()
                stack.pop()
                stack.append(cal(l, r, c))
            print(stack, c)

        return stack[0]

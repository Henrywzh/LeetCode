class Solution:
    def isValid(self, s: str) -> bool:
        check = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for c in s:
            if c in check.values():
                if stack and check[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

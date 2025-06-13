class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not self.isValidChar(s[l]):
                l += 1
                continue
            if not self.isValidChar(s[r]):
                r -= 1
                continue

            left = s[l].lower()
            right = s[r].lower()

            if left != right:
                return False

            l += 1
            r -= 1

        return True

    def isValidChar(self, c: str) -> bool:
        if (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')):
            return True
        elif ord('0') <= ord(c) <= ord('9'):
            return True
        else:
            return False

